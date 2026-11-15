"""Controlled experiment for A13.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8) if bad else (8 - 6)
print(repr(result))
