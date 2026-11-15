"""Controlled experiment for A06.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (24)
print(repr(result))
