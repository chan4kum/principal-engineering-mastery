"""Controlled experiment for A06.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4 + 1) if bad else (max(4, 7) + 1)
print(repr(result))
