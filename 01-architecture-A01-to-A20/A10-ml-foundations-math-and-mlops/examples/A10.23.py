"""Controlled experiment for A10.23. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (3 * 4)
print(repr(result))
