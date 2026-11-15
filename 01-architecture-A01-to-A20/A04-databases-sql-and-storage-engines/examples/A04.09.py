"""Controlled experiment for A04.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2**3) if bad else (100**3)
print(repr(result))
