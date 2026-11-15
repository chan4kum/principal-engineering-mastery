"""Controlled experiment for A10.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (3 * 2)
print(repr(result))
