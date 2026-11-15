"""Controlled experiment for A13.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (3 - 1)
print(repr(result))
