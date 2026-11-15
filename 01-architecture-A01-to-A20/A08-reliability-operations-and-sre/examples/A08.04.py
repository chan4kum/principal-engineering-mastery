"""Controlled experiment for A08.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (100 - 4 - 2)
print(repr(result))
