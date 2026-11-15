"""Controlled experiment for A12.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (3)
print(repr(result))
