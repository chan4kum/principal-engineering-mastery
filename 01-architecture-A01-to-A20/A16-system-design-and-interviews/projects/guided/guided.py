"""Unique opaque redirect mappings backed by SQLite."""

import sqlite3
from urllib.parse import urlsplit


def initialize(db: sqlite3.Connection) -> None:
    db.execute("CREATE TABLE IF NOT EXISTS links (code TEXT PRIMARY KEY, target TEXT NOT NULL)")


def store(db: sqlite3.Connection, code: str, target: str) -> None:
    parsed = urlsplit(target)
    if not (
        code.isascii()
        and code.isalnum()
        and parsed.scheme in {"https", "http"}
        and parsed.hostname
        and parsed.username is None
        and parsed.password is None
    ):
        raise ValueError("invalid link")
    with db:
        db.execute("INSERT INTO links VALUES (?, ?)", (code, target))


def resolve(db: sqlite3.Connection, code: str) -> str | None:
    row = db.execute("SELECT target FROM links WHERE code = ?", (code,)).fetchone()
    return None if row is None else row[0]
