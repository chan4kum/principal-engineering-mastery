"""Controlled experiment for A06.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2**12 + 1) if bad else (2**12)
print(repr(result))
