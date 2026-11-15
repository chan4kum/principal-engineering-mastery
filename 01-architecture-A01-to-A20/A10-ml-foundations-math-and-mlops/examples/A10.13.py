"""Controlled experiment for A10.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (16) if bad else (round((4 - 0.1 * 8) ** 2, 2))
print(repr(result))
