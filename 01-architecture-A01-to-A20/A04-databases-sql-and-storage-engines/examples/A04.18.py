"""Controlled experiment for A04.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12000) if bad else (12000 // 500)
print(repr(result))
