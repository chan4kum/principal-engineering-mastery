"""Controlled experiment for A12.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 / 61) if bad else (round(1 / 61 + 1 / 64, 5))
print(repr(result))
