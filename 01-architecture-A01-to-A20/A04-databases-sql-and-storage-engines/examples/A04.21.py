"""Controlled experiment for A04.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20 / 20) if bad else (2 / 20)
print(repr(result))
