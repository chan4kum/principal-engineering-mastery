"""Controlled experiment for A05.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (800) if bad else (800 / 8)
print(repr(result))
