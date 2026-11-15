"""Controlled experiment for A13.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6) if bad else (6 // 2)
print(repr(result))
