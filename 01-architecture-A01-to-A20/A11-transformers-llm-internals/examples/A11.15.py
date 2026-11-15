"""Controlled experiment for A11.15. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (500) if bad else (1000 / 500)
print(repr(result))
