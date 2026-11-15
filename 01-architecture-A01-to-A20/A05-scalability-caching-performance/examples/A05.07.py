"""Controlled experiment for A05.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200) if bad else (20 / 200)
print(repr(result))
