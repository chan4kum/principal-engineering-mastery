"""Controlled experiment for A09.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (80)
print(repr(result))
