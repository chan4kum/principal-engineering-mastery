"""Controlled experiment for A09.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (10 * 0.5)
print(repr(result))
