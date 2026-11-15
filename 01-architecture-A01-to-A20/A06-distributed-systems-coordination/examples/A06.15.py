"""Controlled experiment for A06.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (50)
print(repr(result))
