"""Controlled experiment for A06.23. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (2)
print(repr(result))
