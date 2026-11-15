"""Controlled experiment for A13.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (4 + 1)
print(repr(result))
