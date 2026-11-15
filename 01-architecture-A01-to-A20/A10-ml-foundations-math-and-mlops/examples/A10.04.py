"""Controlled experiment for A10.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.25) if bad else (2 * 0.25 * 0.75)
print(repr(result))
