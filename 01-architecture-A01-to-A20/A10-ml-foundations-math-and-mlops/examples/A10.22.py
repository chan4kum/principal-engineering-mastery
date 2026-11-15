"""Controlled experiment for A10.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (25) if bad else (25 / 1000)
print(repr(result))
