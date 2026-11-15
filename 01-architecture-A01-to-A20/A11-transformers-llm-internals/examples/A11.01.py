"""Controlled experiment for A11.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 * 3) if bad else (2 * 3 * 2 * 4)
print(repr(result))
