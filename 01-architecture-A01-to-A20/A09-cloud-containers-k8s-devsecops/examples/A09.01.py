"""Controlled experiment for A09.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8) if bad else (25 / 100)
print(repr(result))
