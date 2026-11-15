"""Controlled experiment for A04.03. Run with --break to compare."""

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
            "CREATE TABLE p(id PRIMARY KEY); CREATE TABLE c(pid); INSERT INTO c VALUES (9);",
            "SELECT count(*) FROM c",
        )
    )
    if bad
    else (
        sql(
            "PRAGMA foreign_keys=ON; CREATE TABLE p(id PRIMARY KEY); CREATE TABLE c(pid REFERENCES p(id)); INSERT INTO c VALUES (9);",
            "SELECT count(*) FROM c",
        )
    )
)
print(repr(result))
