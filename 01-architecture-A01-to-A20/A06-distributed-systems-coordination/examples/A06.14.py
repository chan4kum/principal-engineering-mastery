"""Controlled experiment for A06.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 + 3 > 5) if bad else (3 + 3 > 5)
print(repr(result))
