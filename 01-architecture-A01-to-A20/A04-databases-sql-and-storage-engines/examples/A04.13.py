"""Controlled experiment for A04.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5 - 1) if bad else (5 - 2)
print(repr(result))
