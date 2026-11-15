"""Controlled experiment for A05.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.75) if bad else (1 / 4)
print(repr(result))
