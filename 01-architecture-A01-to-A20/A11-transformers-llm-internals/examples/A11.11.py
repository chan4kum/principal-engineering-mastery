"""Controlled experiment for A11.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (5 + 3)
print(repr(result))
