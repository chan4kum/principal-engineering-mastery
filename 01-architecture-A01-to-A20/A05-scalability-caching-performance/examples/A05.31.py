"""Controlled experiment for A05.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (300 - 150) if bad else (300 - 60 - 150)
print(repr(result))
