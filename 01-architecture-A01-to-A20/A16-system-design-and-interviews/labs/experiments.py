"""Test one-machine design and business invariants."""

import sqlite3
from contextlib import closing

import guided
import independent


def observe(lab, broken):
    with closing(sqlite3.connect(":memory:")) as db:
        if lab == 1:
            guided.initialize(db)
            guided.store(db, "ref", "https://example.test/item")
            return guided.resolve(db, "missing" if broken else "ref")
        if lab == 2:
            return independent.sizing(86400, 100, 2, 1 if broken else 3)
        independent.initialize(db)
        assert independent.reserve(db, "key-a", "seat-a")
        if lab == 3:
            try:
                independent.reserve(db, "key-a", "seat-b" if broken else "seat-a")
            except ValueError:
                return "idempotency conflict"
            return "same result"
        return independent.reserve(db, "key-b", "seat-a" if broken else "seat-b")


EXPECTED = (
    ("https://example.test/item", None),
    ((1.0, 51840000), (1.0, 17280000)),
    ("same result", "idempotency conflict"),
    (True, False),
)
