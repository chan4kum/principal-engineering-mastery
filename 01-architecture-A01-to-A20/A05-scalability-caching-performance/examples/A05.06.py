"""Controlled experiment for A05.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 / 100) if bad else (1 / (100 - 90))
print(repr(result))
