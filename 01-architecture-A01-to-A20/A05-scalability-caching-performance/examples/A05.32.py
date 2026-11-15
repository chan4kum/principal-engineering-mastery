"""Controlled experiment for A05.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (700 / 800) if bad else (700 / 1000)
print(repr(result))
