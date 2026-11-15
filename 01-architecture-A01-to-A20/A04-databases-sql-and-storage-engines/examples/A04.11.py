"""Controlled experiment for A04.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (len({("T1", "T2"), ("T2", "T1")})) if bad else (len({("T2", "T1")}))
print(repr(result))
