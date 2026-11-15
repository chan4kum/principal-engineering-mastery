"""Controlled experiment for A07.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (100 - 80)
print(repr(result))
