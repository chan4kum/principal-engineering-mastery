"""Controlled experiment for A11.35. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (1000 * 4 / 100)
print(repr(result))
