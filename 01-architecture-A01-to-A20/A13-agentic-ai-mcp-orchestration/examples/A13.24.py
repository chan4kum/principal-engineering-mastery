"""Controlled experiment for A13.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (7) if bad else (2)
print(repr(result))
