"""Controlled experiment for A08.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (60 * 5) if bad else (0)
print(repr(result))
