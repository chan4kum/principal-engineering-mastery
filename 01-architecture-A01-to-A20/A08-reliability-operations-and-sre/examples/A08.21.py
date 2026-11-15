"""Controlled experiment for A08.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (100 * 2)
print(repr(result))
