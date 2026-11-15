"""Controlled experiment for A12.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (100 * 20)
print(repr(result))
