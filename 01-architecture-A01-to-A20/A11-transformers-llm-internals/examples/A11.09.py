"""Controlled experiment for A11.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ((1, 3)) if bad else ((-1, 1))
print(repr(result))
