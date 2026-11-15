"""Async API with transactional idempotency and request correlation."""

import asyncio
from collections.abc import Callable, Mapping
from contextlib import closing
from contextvars import ContextVar
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import time
from uuid import uuid4

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, ConfigDict, Field

correlation: ContextVar[str] = ContextVar("correlation")
SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY, tenant TEXT NOT NULL, label TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS receipts (
    tenant TEXT NOT NULL, request_key TEXT NOT NULL, digest TEXT NOT NULL,
    response_json TEXT NOT NULL, PRIMARY KEY (tenant, request_key)
);
"""


class Command(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    label: str = Field(min_length=1, max_length=80)


class Conflict(Exception):
    """An idempotency key already describes different content."""


def record(db: Path, tenant: str, key: str, label: str) -> tuple[str, bool]:
    payload = json.dumps({"label": label}, ensure_ascii=False, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    with closing(sqlite3.connect(db, timeout=4)) as connection, connection:
        connection.execute("BEGIN IMMEDIATE")
        previous = connection.execute(
            "SELECT digest,response_json FROM receipts WHERE tenant=? AND request_key=?",
            (tenant, key),
        ).fetchone()
        if previous is not None:
            if previous[0] != digest:
                raise Conflict
            return previous[1], True
        job_id = uuid4().hex
        body = json.dumps({"id": job_id, "label": label}, ensure_ascii=False)
        connection.execute("INSERT INTO jobs VALUES (?,?,?)", (job_id, tenant, label))
        connection.execute("INSERT INTO receipts VALUES (?,?,?,?)", (tenant, key, digest, body))
        return body, False


def create_app(
    db: Path,
    tokens: Mapping[str, str],
    emit: Callable[[dict[str, object]], None] | None = None,
) -> FastAPI:
    with closing(sqlite3.connect(db)) as connection:
        connection.executescript(SCHEMA)
    app = FastAPI(title="Local job intake")
    identities = dict(tokens)
    pending: set[asyncio.Task[tuple[str, bool]]] = set()
    slots = 8

    def conclude(job: asyncio.Task[tuple[str, bool]]) -> None:
        pending.discard(job)
        if not job.cancelled():
            # Retrieve the result or exception if the caller disconnected.
            job.exception()

    @app.middleware("http")
    async def request_scope(request: Request, call_next):
        request_id = uuid4().hex
        reset = correlation.set(request_id)
        start = time.monotonic()
        status = None
        try:
            response = await call_next(request)
            status = response.status_code
            response.headers["X-Request-ID"] = request_id
            return response
        finally:
            correlation.reset(reset)
            if emit is not None:
                emit(
                    {
                        "request_id": request_id,
                        "method": request.method,
                        "route": getattr(request.scope.get("route"), "path", None),
                        "status": status,
                        "elapsed_ms": (time.monotonic() - start) * 1000,
                    }
                )

    @app.post("/jobs", status_code=201)
    async def submit(
        command: Command,
        authorization: str = Header(default=""),
        idempotency_key: str = Header(default=""),
    ) -> Response:
        scheme, _, secret = authorization.partition(" ")
        tenant = identities.get(secret) if scheme.lower() == "bearer" else None
        if tenant is None:
            raise HTTPException(
                401, "Valid fixture credential required", headers={"WWW-Authenticate": "Bearer"}
            )
        if re.fullmatch(r"[A-Za-z0-9_-]{1,80}", idempotency_key) is None:
            raise HTTPException(400, "A 1–80 character Idempotency-Key is required")
        if len(pending) >= slots:
            raise HTTPException(503, "Local job admission full", headers={"Retry-After": "1"})
        job = asyncio.create_task(
            asyncio.to_thread(record, db, tenant, idempotency_key, command.label)
        )
        pending.add(job)
        job.add_done_callback(conclude)
        try:
            body, replay = await asyncio.shield(job)
        except Conflict as error:
            raise HTTPException(409, "Idempotency key has different content") from error
        except sqlite3.OperationalError as error:
            if getattr(error, "sqlite_errorcode", None) != sqlite3.SQLITE_BUSY:
                raise
            raise HTTPException(503, "Local store busy", headers={"Retry-After": "1"}) from error
        return Response(
            body,
            status_code=201,
            media_type="application/json",
            headers={
                "Idempotency-Replayed": str(replay).lower(),
                "Location": f"/jobs/{json.loads(body)['id']}",
                "X-Request-ID": correlation.get(),
            },
        )

    return app
