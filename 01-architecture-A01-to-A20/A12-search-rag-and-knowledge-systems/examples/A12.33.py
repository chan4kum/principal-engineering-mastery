"""Controlled experiment for A12.33. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (500) if bad else (500 // 5)
print(repr(result))
