"""Controlled experiment for A05.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (10 - 8)
print(repr(result))
