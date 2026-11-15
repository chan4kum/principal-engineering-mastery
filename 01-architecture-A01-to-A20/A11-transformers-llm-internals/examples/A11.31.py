"""Controlled experiment for A11.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2000) if bad else (2000 // 100)
print(repr(result))
