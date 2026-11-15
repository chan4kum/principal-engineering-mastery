"""Controlled experiment for A05.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (250) if bad else (max(0, 250 - 200))
print(repr(result))
