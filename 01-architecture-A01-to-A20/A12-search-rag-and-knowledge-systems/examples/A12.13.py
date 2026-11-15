"""Controlled experiment for A12.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (10 - 4)
print(repr(result))
