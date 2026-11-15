"""Controlled experiment for A09.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2000) if bad else (2000 // 250)
print(repr(result))
