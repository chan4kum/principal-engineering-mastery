"""Controlled experiment for A04.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
records = [("k", 3), ("k", 8)]
keydir = {key: offset for key, offset in records}
print(records[0][1] if bad else keydir["k"])
