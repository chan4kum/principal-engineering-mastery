"""Controlled experiment for A05.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.99) if bad else (round(0.99**10, 4))
print(repr(result))
