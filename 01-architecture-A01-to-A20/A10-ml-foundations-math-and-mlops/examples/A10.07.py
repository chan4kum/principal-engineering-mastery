"""Controlled experiment for A10.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000) if bad else (1000 * 15 // 100)
print(repr(result))
