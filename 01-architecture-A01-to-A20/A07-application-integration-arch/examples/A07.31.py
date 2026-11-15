"""Controlled experiment for A07.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (5 * 4)
print(repr(result))
