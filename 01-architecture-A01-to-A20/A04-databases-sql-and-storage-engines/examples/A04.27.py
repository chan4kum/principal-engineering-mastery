"""Controlled experiment for A04.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
flushed = {"k": 4}
memtable = {"k": 9}
print(flushed["k"] if bad else memtable.get("k", flushed["k"]))
