"""Single-authority local coordinator with durable fences and replay receipts."""

import sqlite3
from contextlib import closing, contextmanager
from pathlib import Path


class Denied(Exception):
    """A lease is occupied, expired, or superseded."""


class Conflict(Exception):
    """An operation ID was reused with a different delta."""


class Coordinator:
    def __init__(self, path: Path) -> None:
        self.path = path
        with closing(sqlite3.connect(path)) as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS resources (
                    name TEXT PRIMARY KEY, owner TEXT NOT NULL, fence INT NOT NULL,
                    expires INT NOT NULL, value INT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS receipts (
                    name TEXT NOT NULL, operation TEXT NOT NULL, delta INT NOT NULL,
                    outcome INT NOT NULL, PRIMARY KEY (name, operation)
                );
            """)

    @contextmanager
    def transaction(self):
        with closing(sqlite3.connect(self.path, timeout=3)) as db, db:
            db.execute("BEGIN IMMEDIATE")
            yield db

    def claim(self, name: str, owner: str, now: int, ttl: int) -> int:
        if ttl <= 0:
            raise ValueError("positive TTL required")
        with self.transaction() as db:
            current = db.execute(
                "SELECT fence, expires FROM resources WHERE name=?", (name,)
            ).fetchone()
            if current is None:
                fence = 1
                db.execute(
                    "INSERT INTO resources VALUES (?, ?, ?, ?, 0)",
                    (name, owner, fence, now + ttl),
                )
            else:
                previous, expires = current
                if now < expires:
                    raise Denied("lease occupied")
                fence = previous + 1
                db.execute(
                    "UPDATE resources SET owner=?, fence=?, expires=? WHERE name=?",
                    (owner, fence, now + ttl, name),
                )
            return fence

    def apply(self, name: str, fence: int, operation: str, delta: int, now: int) -> int:
        with self.transaction() as db:
            resource = db.execute(
                "SELECT fence, expires, value FROM resources WHERE name=?", (name,)
            ).fetchone()
            if resource is None or resource[0] != fence or now >= resource[1]:
                raise Denied("stale or expired fence")
            previous = db.execute(
                "SELECT delta, outcome FROM receipts WHERE name=? AND operation=?",
                (name, operation),
            ).fetchone()
            if previous is not None:
                if previous[0] != delta:
                    raise Conflict("operation ID changed payload")
                return previous[1]
            total = resource[2] + delta
            db.execute("UPDATE resources SET value=? WHERE name=?", (total, name))
            db.execute(
                "INSERT INTO receipts VALUES (?, ?, ?, ?)",
                (name, operation, delta, total),
            )
            return total

    def value(self, name: str) -> int:
        with closing(sqlite3.connect(self.path)) as db:
            row = db.execute(
                "SELECT value FROM resources WHERE name=?", (name,)
            ).fetchone()
            return row[0] if row is not None else 0
