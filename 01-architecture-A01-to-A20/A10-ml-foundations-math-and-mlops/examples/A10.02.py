"""Controlled experiment for A10.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ((3, 2)) if bad else ((4, 2))
print(repr(result))
