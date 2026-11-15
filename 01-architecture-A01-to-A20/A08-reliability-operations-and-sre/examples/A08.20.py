"""Controlled experiment for A08.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12) if bad else (12 - 5)
print(repr(result))
