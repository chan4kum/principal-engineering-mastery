"""Controlled experiment for A06.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (25 - 30) if bad else (12 - 9)
print(repr(result))
