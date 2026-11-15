"""Controlled experiment for A10.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1001000) if bad else (1000)
print(repr(result))
