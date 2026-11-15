"""Durable queue fixture with a worker that can exit before acknowledging."""

import argparse
import os
import sqlite3
from contextlib import closing
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException, Response


def initialize(path: Path) -> None:
    with closing(sqlite3.connect(path)) as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, status TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS effects (job INTEGER PRIMARY KEY);
        """)


def run_worker(path: Path, crash: bool = False) -> int | None:
    with closing(sqlite3.connect(path)) as db:
        with db:
            db.execute("BEGIN IMMEDIATE")
            next_job = db.execute(
                "SELECT id FROM jobs WHERE status='pending' ORDER BY id LIMIT 1"
            ).fetchone()
            if next_job is None:
                return None
            job = next_job[0]
            db.execute("INSERT OR IGNORE INTO effects VALUES (?)", (job,))
        # The durable business effect exists before the separate acknowledgement.
        if crash:
            os._exit(75)
        with db:
            db.execute("UPDATE jobs SET status='done' WHERE id=?", (job,))
        return job


def create_app(path: Path, dependency: FastAPI) -> FastAPI:
    initialize(path)
    app = FastAPI()

    @app.post("/checkout/synchronous")
    async def synchronous() -> dict[str, int]:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=dependency),
            base_url="http://dependency.test",
        ) as client:
            stock = await client.get("/inventory")
            if stock.status_code != 200:
                raise HTTPException(503, "Inventory unavailable")
            price = await client.get("/price")
            if price.status_code != 200:
                raise HTTPException(503, "Pricing unavailable")
        return {"total_cents": price.json()["cents"]}

    @app.post("/checkout/queued", status_code=202)
    def queued(response: Response) -> dict[str, int]:
        with closing(sqlite3.connect(path)) as db, db:
            job = db.execute("INSERT INTO jobs(status) VALUES ('pending')").lastrowid
        response.headers["Location"] = f"/jobs/{job}"
        return {"id": job}

    @app.get("/jobs/{job}")
    def status(job: int) -> dict[str, str]:
        with closing(sqlite3.connect(path)) as db:
            row = db.execute("SELECT status FROM jobs WHERE id=?", (job,)).fetchone()
        if row is None:
            raise HTTPException(404, "Unknown job")
        return {"status": row[0]}

    return app


if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    cli.add_argument("database", type=Path)
    cli.add_argument("--exit-before-ack", action="store_true")
    args = cli.parse_args()
    print(run_worker(args.database, args.exit_before_ack))
