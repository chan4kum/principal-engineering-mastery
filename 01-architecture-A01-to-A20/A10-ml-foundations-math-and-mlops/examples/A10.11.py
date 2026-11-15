"""Controlled experiment for A10.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8 / (8 + 2)) if bad else (8 / (8 + 12))
print(repr(result))
