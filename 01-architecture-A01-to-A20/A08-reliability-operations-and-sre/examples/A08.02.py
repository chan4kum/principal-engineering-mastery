"""Controlled experiment for A08.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100000) if bad else (100000 // 1000)
print(repr(result))
