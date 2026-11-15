"""Controlled experiment for A10.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (20 / 1000)
print(repr(result))
