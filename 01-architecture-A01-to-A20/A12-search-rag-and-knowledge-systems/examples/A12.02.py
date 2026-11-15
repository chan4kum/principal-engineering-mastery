"""Controlled experiment for A12.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (1)
print(repr(result))
