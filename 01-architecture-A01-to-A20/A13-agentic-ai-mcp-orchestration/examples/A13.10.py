"""Controlled experiment for A13.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5) if bad else (5 - 3)
print(repr(result))
