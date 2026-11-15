"""Controlled experiment for A08.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (60000) if bad else (60000 // 2000)
print(repr(result))
