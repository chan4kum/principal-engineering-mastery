"""Controlled experiment for A06.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5 + 5) if bad else (5)
print(repr(result))
