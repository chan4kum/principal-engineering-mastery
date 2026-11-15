"""Controlled experiment for A04.05. Run with --break to compare."""

import sqlite3
import sys
from contextlib import closing


def sql(setup: str, query: str) -> int | str:
    with closing(sqlite3.connect(":memory:")) as connection:
        try:
            connection.executescript(setup)
        except sqlite3.IntegrityError:
            return "rejected"
        return connection.execute(query).fetchone()[0]


bad = "--break" in sys.argv[1:]
result = (
    (
        sql(
            "CREATE TABLE l(i); INSERT INTO l VALUES (1),(1),(2),(2),(3),(3);",
            "SELECT count(*) FROM l",
        )
    )
    if bad
    else (
        sql(
            "CREATE TABLE l(i); INSERT INTO l VALUES (1),(1),(2),(2),(3),(3);",
            "SELECT count(DISTINCT i) FROM l",
        )
    )
)
print(repr(result))
