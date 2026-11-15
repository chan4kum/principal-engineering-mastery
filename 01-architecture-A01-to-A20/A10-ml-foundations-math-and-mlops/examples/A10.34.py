"""Controlled experiment for A10.34. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000) if bad else (1000 // 10)
print(repr(result))
