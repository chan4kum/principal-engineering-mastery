"""Controlled experiment for A04.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000 * 4) if bad else (1000 * 4 / 200)
print(repr(result))
