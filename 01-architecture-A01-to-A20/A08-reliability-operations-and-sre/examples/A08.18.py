"""Controlled experiment for A08.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (240) if bad else (240 * 1024 // 120)
print(repr(result))
