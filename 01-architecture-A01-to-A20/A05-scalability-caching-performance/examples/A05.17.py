"""Controlled experiment for A05.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8 * 15) if bad else (80 // 8)
print(repr(result))
