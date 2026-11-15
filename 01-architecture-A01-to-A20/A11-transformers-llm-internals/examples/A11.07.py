"""Controlled experiment for A11.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (7) if bad else (7 + 3)
print(repr(result))
