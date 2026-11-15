"""Controlled experiment for A12.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000) if bad else (1000 * 16)
print(repr(result))
