"""Controlled experiment for A13.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (4 - 1)
print(repr(result))
