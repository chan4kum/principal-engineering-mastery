"""Controlled experiment for A05.34. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12 * 10) if bad else (80 // 12)
print(repr(result))
