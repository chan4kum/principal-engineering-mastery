"""Controlled experiment for A08.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (30) if bad else (30 - 5 - 2)
print(repr(result))
