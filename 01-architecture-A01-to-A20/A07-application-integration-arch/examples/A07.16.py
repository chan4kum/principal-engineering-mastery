"""Controlled experiment for A07.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000) if bad else (10000 - 9000)
print(repr(result))
