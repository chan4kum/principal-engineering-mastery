"""Controlled experiment for A05.33. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (600 // 200) if bad else (600 // 200 + 1)
print(repr(result))
