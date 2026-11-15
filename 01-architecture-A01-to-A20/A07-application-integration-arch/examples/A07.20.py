"""Controlled experiment for A07.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8) if bad else (min(8, 4))
print(repr(result))
