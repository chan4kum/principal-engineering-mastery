"""Controlled experiment for A13.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (2)
print(repr(result))
