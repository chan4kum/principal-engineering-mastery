"""Controlled experiment for A04.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8192 // 120) if bad else ((8192 - 24) // 124)
print(repr(result))
