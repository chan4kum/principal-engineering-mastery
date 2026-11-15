"""Controlled experiment for A06.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6) if bad else (3)
print(repr(result))
