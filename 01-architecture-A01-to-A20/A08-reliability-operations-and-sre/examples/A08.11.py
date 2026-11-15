"""Controlled experiment for A08.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (120) if bad else (120 - 60)
print(repr(result))
