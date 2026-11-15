"""Controlled experiment for A04.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4096 / 100) if bad else (2048 / 100)
print(repr(result))
