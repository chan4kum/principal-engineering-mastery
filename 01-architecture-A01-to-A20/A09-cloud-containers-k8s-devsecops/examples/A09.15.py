"""Controlled experiment for A09.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (2)
print(repr(result))
