"""Controlled experiment for A08.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2000) if bad else (2000 * 5 // 100)
print(repr(result))
