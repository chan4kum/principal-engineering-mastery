"""Controlled experiment for A11.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (3 / 5)
print(repr(result))
