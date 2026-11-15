"""Controlled experiment for A07.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4800) if bad else (4800 // 400)
print(repr(result))
