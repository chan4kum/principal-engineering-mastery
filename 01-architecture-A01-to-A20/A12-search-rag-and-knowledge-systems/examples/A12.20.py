"""Controlled experiment for A12.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 / 5) if bad else (1 / 4)
print(repr(result))
