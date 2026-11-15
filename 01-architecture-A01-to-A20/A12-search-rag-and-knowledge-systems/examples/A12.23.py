"""Controlled experiment for A12.23. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (1 + 3)
print(repr(result))
