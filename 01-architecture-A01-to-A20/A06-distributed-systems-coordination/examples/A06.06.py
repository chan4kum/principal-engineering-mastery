"""Controlled experiment for A06.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (6)
print(repr(result))
