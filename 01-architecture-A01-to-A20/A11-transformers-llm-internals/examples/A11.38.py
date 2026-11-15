"""Controlled experiment for A11.38. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12 / 1000) if bad else (12 / 800)
print(repr(result))
