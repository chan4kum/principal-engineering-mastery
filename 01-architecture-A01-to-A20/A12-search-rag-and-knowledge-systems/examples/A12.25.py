"""Controlled experiment for A12.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (40) if bad else (10)
print(repr(result))
