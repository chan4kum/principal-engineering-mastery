"""Controlled experiment for A08.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000 // 100) if bad else (10 / 100)
print(repr(result))
