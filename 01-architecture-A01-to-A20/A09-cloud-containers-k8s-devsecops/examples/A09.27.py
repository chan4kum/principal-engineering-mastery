"""Controlled experiment for A09.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (4)
print(repr(result))
