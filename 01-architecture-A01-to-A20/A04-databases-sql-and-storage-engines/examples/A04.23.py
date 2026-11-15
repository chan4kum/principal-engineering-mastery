"""Controlled experiment for A04.23. Run with --break to compare."""

import dbm
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def disk(persist: bool) -> str | None:
    if not persist:
        lookup = {}
        lookup["k"] = "durable"
        return {}.get("k")
    with TemporaryDirectory() as directory:
        path = str(Path(directory) / "database")
        with dbm.open(path, "c") as database:
            database[b"k"] = b"durable"
        with dbm.open(path, "r") as database:
            return database[b"k"].decode()


bad = "--break" in sys.argv[1:]
result = (disk(False)) if bad else (disk(True))
print(repr(result))
