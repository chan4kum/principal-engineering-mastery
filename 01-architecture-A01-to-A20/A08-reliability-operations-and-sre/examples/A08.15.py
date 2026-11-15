"""Controlled experiment for A08.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.01) if bad else (0.01 / 0.001)
print(repr(result))
