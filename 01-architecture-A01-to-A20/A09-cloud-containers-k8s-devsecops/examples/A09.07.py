"""Controlled experiment for A09.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (2)
print(repr(result))
