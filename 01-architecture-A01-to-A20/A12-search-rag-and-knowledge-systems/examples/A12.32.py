"""Controlled experiment for A12.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (80) if bad else (80 - 60)
print(repr(result))
