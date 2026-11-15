"""Controlled experiment for A09.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20 * 15) if bad else (0)
print(repr(result))
