"""Controlled experiment for A12.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (4 * 3)
print(repr(result))
