"""Controlled experiment for A10.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (14) if bad else (float((14 - 10) / 2))
print(repr(result))
