"""Controlled experiment for A10.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12) if bad else (12 - 10)
print(repr(result))
