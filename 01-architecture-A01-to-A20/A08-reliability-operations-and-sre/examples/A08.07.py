"""Controlled experiment for A08.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (300) if bad else (300 - 60 - 30)
print(repr(result))
