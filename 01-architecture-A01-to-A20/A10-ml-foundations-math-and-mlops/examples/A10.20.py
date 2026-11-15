"""Controlled experiment for A10.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (14 - 10) if bad else ((14 - 10) / 2)
print(repr(result))
