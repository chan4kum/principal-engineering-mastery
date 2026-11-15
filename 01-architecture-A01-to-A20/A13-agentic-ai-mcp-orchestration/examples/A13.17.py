"""Controlled experiment for A13.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (2)
print(repr(result))
