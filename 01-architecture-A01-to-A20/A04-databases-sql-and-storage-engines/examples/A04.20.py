"""Controlled experiment for A04.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20 * 90) if bad else (20 * 30)
print(repr(result))
