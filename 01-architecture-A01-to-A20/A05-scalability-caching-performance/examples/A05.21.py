"""Controlled experiment for A05.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (10)
print(repr(result))
