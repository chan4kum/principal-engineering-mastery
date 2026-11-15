"""Controlled experiment for A09.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12) if bad else (2)
print(repr(result))
