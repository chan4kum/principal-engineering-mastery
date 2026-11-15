"""Controlled experiment for A05.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (400) if bad else (4)
print(repr(result))
