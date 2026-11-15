"""Controlled experiment for A05.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 / 0.1) if bad else (5 / 0.1)
print(repr(result))
