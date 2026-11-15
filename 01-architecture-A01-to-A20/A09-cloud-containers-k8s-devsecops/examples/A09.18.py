"""Controlled experiment for A09.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 // 1) if bad else (2000 // 250)
print(repr(result))
