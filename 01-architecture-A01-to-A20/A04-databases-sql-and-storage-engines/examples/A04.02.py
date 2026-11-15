"""Controlled experiment for A04.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 + 8) if bad else (8 + 8)
print(repr(result))
