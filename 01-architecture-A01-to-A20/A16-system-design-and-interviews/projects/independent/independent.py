"""Transaction-critical prototype with payload-bound idempotency."""

import sqlite3


def initialize(db: sqlite3.Connection) -> None:
    db.execute("""CREATE TABLE IF NOT EXISTS bookings (
        idempotency_key TEXT PRIMARY KEY, seat TEXT NOT NULL, committed INTEGER NOT NULL
    )""")
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS sold_seat ON bookings(seat) WHERE committed=1")


def reserve(db: sqlite3.Connection, key: str, seat: str) -> bool:
    if not key or not seat or db.in_transaction:
        raise ValueError("nonempty request fields and a fresh transaction required")
    db.execute("BEGIN IMMEDIATE")
    with db:
        prior = db.execute(
            "SELECT seat, committed FROM bookings WHERE idempotency_key = ?", (key,)
        ).fetchone()
        if prior:
            if prior[0] != seat:
                raise ValueError("idempotency conflict")
            return bool(prior[1])
        sold = db.execute("SELECT 1 FROM bookings WHERE seat=? AND committed=1", (seat,)).fetchone()
        db.execute("INSERT INTO bookings VALUES (?, ?, ?)", (key, seat, int(sold is None)))
        return sold is None


def sizing(per_day: int, bytes_per_row: int, days: int, replicas: int):
    if min(per_day, bytes_per_row, days) < 0 or replicas < 1:
        raise ValueError("invalid capacity inputs")
    return (per_day / 86400, per_day * bytes_per_row * days * replicas)
