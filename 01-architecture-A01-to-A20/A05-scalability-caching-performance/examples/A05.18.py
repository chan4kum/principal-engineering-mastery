"""Controlled experiment for A05.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (8)
print(repr(result))
