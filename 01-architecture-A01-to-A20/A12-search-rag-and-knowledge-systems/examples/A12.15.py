"""Controlled experiment for A12.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1.0) if bad else (8 / 10)
print(repr(result))
