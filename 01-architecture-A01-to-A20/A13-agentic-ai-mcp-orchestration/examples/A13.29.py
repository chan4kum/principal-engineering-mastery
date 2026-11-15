"""Controlled experiment for A13.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (20 // 5)
print(repr(result))
