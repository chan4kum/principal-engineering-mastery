"""Controlled experiment for A05.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 + 20) if bad else (2 + (100 - 90) * 20 / 100)
print(repr(result))
