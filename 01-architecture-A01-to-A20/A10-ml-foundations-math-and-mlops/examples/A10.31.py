"""Controlled experiment for A10.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.9) if bad else ((0.9 + 0.6) / 2)
print(repr(result))
