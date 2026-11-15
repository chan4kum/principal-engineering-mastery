"""Controlled experiment for A12.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (0)
print(repr(result))
