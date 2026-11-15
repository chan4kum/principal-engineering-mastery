"""Controlled experiment for A05.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000 / 100) if bad else (1000 / (100 - 80))
print(repr(result))
