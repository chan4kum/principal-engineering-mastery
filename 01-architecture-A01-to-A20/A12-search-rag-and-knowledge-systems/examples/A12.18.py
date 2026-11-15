"""Controlled experiment for A12.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (50 * 2)
print(repr(result))
