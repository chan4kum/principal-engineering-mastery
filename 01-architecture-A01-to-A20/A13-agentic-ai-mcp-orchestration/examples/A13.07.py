"""Controlled experiment for A13.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000) if bad else (10000 - 1500)
print(repr(result))
