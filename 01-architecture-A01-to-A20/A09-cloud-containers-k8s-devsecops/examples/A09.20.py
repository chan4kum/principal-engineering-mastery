"""Controlled experiment for A09.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (3 * 20)
print(repr(result))
