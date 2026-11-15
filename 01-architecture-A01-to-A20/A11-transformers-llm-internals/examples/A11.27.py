"""Controlled experiment for A11.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (32000) if bad else (32000 // 2)
print(repr(result))
