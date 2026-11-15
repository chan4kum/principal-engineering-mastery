"""Controlled experiment for A08.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000) if bad else (1000 // 10)
print(repr(result))
