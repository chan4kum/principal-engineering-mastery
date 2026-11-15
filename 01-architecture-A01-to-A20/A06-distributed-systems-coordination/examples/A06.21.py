"""Controlled experiment for A06.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10 + 3 + 3) if bad else (10 + 3)
print(repr(result))
