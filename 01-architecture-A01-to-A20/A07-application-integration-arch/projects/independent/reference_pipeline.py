"""Local saga, durable outbox and idempotent consumer across two SQLite files."""

import json
import sqlite3
from collections.abc import Iterator
from contextlib import closing, contextmanager
from pathlib import Path
from typing import ClassVar


class SimulatedFailure(Exception):
    """A controlled stopping point between independent commits."""


@contextmanager
def transaction(file: Path) -> Iterator[sqlite3.Connection]:
    with closing(sqlite3.connect(file, timeout=3)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        yield db


class Pipeline:
    """Fixed transitions with explicit durable checkpoints and replay IDs."""

    transitions: ClassVar[dict[str, tuple[str, str]]] = {
        "submitted": ("reserve", "reserved"),
        "reserved": ("charge", "charged"),
        "compensating": ("refund", "refunded"),
        "refunded": ("release", "cancelled"),
    }

    def __init__(self, database: Path, broker: Path) -> None:
        if database.resolve() == broker.resolve():
            raise ValueError("database and broker must be distinct stores")
        self.database = database
        self.broker = broker
        with closing(sqlite3.connect(database)) as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS orders (
                    tenant TEXT NOT NULL, id TEXT NOT NULL, state TEXT NOT NULL,
                    PRIMARY KEY (tenant, id)
                );
                CREATE TABLE IF NOT EXISTS effects (
                    tenant TEXT NOT NULL, id TEXT NOT NULL, kind TEXT NOT NULL,
                    PRIMARY KEY (tenant, id, kind)
                );
                CREATE TABLE IF NOT EXISTS outbox (
                    seq INTEGER PRIMARY KEY, event_id TEXT NOT NULL UNIQUE,
                    payload TEXT NOT NULL, sent INTEGER NOT NULL DEFAULT 0
                );
            """)
        with closing(sqlite3.connect(broker)) as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS deliveries (
                    seq INTEGER PRIMARY KEY, event_id TEXT NOT NULL, payload TEXT NOT NULL,
                    acked INTEGER NOT NULL DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS projection (
                    event_id TEXT PRIMARY KEY, payload TEXT NOT NULL
                );
            """)

    @staticmethod
    def enqueue(db: sqlite3.Connection, tenant: str, order: str, state: str) -> None:
        fields = (tenant, order, state)
        event_id = json.dumps(fields, separators=(",", ":"))
        payload = json.dumps(
            dict(zip(("tenant", "order", "state"), fields, strict=True))
        )
        db.execute(
            "INSERT INTO outbox(event_id,payload) VALUES (?,?)", (event_id, payload)
        )

    def submit(self, tenant: str, order: str) -> bool:
        with transaction(self.database) as db:
            inserted = db.execute(
                "INSERT OR IGNORE INTO orders VALUES (?,?,'submitted')", (tenant, order)
            ).rowcount
            if inserted:
                self.enqueue(db, tenant, order, "submitted")
            return bool(inserted)

    def advance(
        self, tenant: str, order: str, *, fail_confirmation: bool = False
    ) -> str:
        with transaction(self.database) as db:
            row = db.execute(
                "SELECT state FROM orders WHERE tenant=? AND id=?", (tenant, order)
            ).fetchone()
            if row is None:
                raise KeyError((tenant, order))
            state = row[0]
            if state in {"complete", "cancelled"}:
                return state
            if state == "charged":
                action, next_state = (
                    (None, "compensating")
                    if fail_confirmation
                    else ("confirm", "complete")
                )
            else:
                action, next_state = self.transitions[state]
            if action is not None:
                db.execute(
                    "INSERT OR IGNORE INTO effects VALUES (?,?,?)",
                    (tenant, order, action),
                )
            db.execute(
                "UPDATE orders SET state=? WHERE tenant=? AND id=?",
                (next_state, tenant, order),
            )
            if next_state in {"complete", "cancelled"}:
                self.enqueue(db, tenant, order, next_state)
            return next_state

    def publish_one(self, *, fail_after_publish: bool = False) -> bool:
        with closing(sqlite3.connect(self.database)) as db:
            row = db.execute(
                "SELECT seq,event_id,payload FROM outbox WHERE sent=0 ORDER BY seq LIMIT 1"
            ).fetchone()
        if row is None:
            return False
        seq, event_id, payload = row
        with transaction(self.broker) as broker:
            broker.execute(
                "INSERT INTO deliveries(event_id,payload) VALUES (?,?)",
                (event_id, payload),
            )
        if fail_after_publish:
            raise SimulatedFailure("publisher stopped before marking its outbox row")
        with transaction(self.database) as db:
            db.execute("UPDATE outbox SET sent=1 WHERE seq=?", (seq,))
        return True

    def consume_one(self, *, fail_after_effect: bool = False) -> bool:
        with transaction(self.broker) as db:
            row = db.execute(
                "SELECT seq, event_id, payload FROM deliveries WHERE acked=0 ORDER BY seq LIMIT 1"
            ).fetchone()
            if row is None:
                return False
            seq, event_id, payload = row
            db.execute(
                "INSERT OR IGNORE INTO projection VALUES (?,?)", (event_id, payload)
            )
        if fail_after_effect:
            raise SimulatedFailure("consumer stopped before acknowledging the delivery")
        with transaction(self.broker) as db:
            db.execute("UPDATE deliveries SET acked=1 WHERE seq=?", (seq,))
        return True
