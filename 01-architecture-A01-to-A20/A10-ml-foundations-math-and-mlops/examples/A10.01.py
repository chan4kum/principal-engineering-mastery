"""Controlled experiment for A10.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3 * 2) if bad else (2**3)
print(repr(result))
