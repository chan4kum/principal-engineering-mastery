"""Controlled experiment for A09.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (4)
print(repr(result))
