"""Controlled experiment for A12.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6) if bad else (1.0)
print(repr(result))
