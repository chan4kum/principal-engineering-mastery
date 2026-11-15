"""Controlled experiment for A05.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (120 * 10) if bad else ((120 - 90) * 10)
print(repr(result))
