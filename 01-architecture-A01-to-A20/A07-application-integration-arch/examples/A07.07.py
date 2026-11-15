"""Controlled experiment for A07.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6) if bad else (1)
print(repr(result))
