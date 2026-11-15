"""Controlled experiment for A06.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (30) if bad else (30 + 10)
print(repr(result))
