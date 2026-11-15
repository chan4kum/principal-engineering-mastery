"""Controlled experiment for A13.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (3)
print(repr(result))
