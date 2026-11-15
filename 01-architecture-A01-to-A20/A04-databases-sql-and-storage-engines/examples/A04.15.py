"""Controlled experiment for A04.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (400) if bad else (400 // 20)
print(repr(result))
