"""Controlled experiment for A05.23. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (len(set(["k"] * 10)))
print(repr(result))
