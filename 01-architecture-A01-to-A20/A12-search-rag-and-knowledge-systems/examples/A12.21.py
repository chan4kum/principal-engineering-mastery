"""Controlled experiment for A12.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1.0) if bad else (7 / 10)
print(repr(result))
