"""Controlled experiment for A11.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (33 // 16) if bad else ((33 + 15) // 16)
print(repr(result))
