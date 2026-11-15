"""Controlled experiment for A10.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.9) if bad else (12 / 20)
print(repr(result))
