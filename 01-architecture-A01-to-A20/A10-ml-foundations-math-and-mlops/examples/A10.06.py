"""Controlled experiment for A10.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (((0 - 2) ** 2 + (4 - 2) ** 2) / 2)
print(repr(result))
