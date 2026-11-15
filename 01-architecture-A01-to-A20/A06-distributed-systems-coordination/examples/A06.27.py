"""Controlled experiment for A06.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.8) if bad else (1 / 5)
print(repr(result))
