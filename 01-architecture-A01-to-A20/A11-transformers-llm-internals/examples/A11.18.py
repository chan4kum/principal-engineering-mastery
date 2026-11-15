"""Controlled experiment for A11.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100 / 2) if bad else (80 / 2)
print(repr(result))
