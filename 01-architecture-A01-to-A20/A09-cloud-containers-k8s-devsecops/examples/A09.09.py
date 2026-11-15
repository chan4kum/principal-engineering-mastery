"""Controlled experiment for A09.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (75 + 150) if bad else (75)
print(repr(result))
