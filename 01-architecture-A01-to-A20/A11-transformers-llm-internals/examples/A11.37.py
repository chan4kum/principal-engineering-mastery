"""Controlled experiment for A11.37. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (25) if bad else (1000 / 25)
print(repr(result))
