"""Verify authorization boundaries, atomic replay and request context."""

import asyncio
from importlib.util import module_from_spec, spec_from_file_location
import os
from pathlib import Path
import sqlite3
import sys

import pytest

pytest.importorskip("fastapi")
import httpx

PHASE = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis"
)


def load(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec and spec.loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_crud_auth_scope_and_schema() -> None:
    api = load("a03_crud", PHASE / "projects/guided/api.py")

    async def exercise():
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=api.app), base_url="http://fixture.test"
        ) as client:
            a = {"Authorization": "Bearer fixture-a-write"}
            read_only = {"Authorization": "Bearer fixture-a-read"}
            b = {"Authorization": "Bearer fixture-b-write"}
            assert (await client.post("/items", json={"title": "A"})).status_code == 401
            assert (await client.post("/items", headers=a, json={"title": 7})).status_code == 422
            assert (
                await client.post("/items", headers=read_only, json={"title": "A"})
            ).status_code == 403
            created = await client.post("/items", headers=a, json={"title": "A"})
            assert created.status_code == 201
            path = created.headers["Location"]
            assert (await client.get(path, headers=b)).status_code == 404
            assert (await client.get(path, headers=read_only)).json() == created.json()
            assert (await client.put(path, headers=a, json={"title": "B"})).json()["title"] == "B"
            assert (await client.delete(path, headers=a)).status_code == 204
            assert (await client.get(path, headers=a)).status_code == 404

    asyncio.run(exercise())


def test_jobs_concurrent_replay_conflict_restart_and_trace(tmp_path: Path) -> None:
    path = Path(os.getenv("A03_API", str(PHASE / "projects/independent/reference_api.py")))
    api = load("a03_jobs", path)
    db = tmp_path / "jobs.sqlite"
    tokens = {"fixture-a": "a", "fixture-b": "b"}
    events = []
    a = {"Authorization": "Bearer fixture-a", "Idempotency-Key": "shared"}
    b = {"Authorization": "Bearer fixture-b", "Idempotency-Key": "shared"}

    async def exercise():
        app = api.create_app(db, tokens, emit=events.append)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
        ) as client:
            receipts = await asyncio.gather(
                *(client.post("/jobs", headers=a, json={"label": "first"}) for _ in range(6))
            )
            assert all(reply.status_code == 201 for reply in receipts)
            first = receipts[0].json()
            assert all(reply.json() == first for reply in receipts)
            assert len({reply.headers["Location"] for reply in receipts}) == 1
            assert sum(reply.headers["Idempotency-Replayed"] == "false" for reply in receipts) == 1
            ids = {reply.headers["X-Request-ID"] for reply in receipts}
            assert len(ids) == 6 and {event["request_id"] for event in events} == ids
            conflict = await client.post("/jobs", headers=a, json={"label": "changed"})
            assert conflict.status_code == 409 and "X-Request-ID" in conflict.headers
            assert (await client.post("/jobs", json={"label": "first"})).status_code == 401
            assert (await client.post("/jobs", headers=a, json={"label": 7})).status_code == 422
            other = await client.post("/jobs", headers=b, json={"label": "first"})
            assert other.status_code == 201 and other.json()["id"] != first["id"]
        restarted = api.create_app(db, tokens)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=restarted), base_url="http://fixture.test"
        ) as client:
            restored = await client.post("/jobs", headers=a, json={"label": "first"})
            assert restored.json() == first
            assert restored.headers["Idempotency-Replayed"] == "true"

    asyncio.run(exercise())
    assert all(event["elapsed_ms"] >= 0 and event["route"] == "/jobs" for event in events)
    assert all("fixture-a" not in repr(event) for event in events)
    with sqlite3.connect(db) as connection:
        assert connection.execute(
            "SELECT tenant, COUNT(*) FROM jobs GROUP BY tenant"
        ).fetchall() == [("a", 1), ("b", 1)]
