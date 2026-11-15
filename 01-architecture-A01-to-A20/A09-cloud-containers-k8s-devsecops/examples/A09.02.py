"""Controlled experiment for A09.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (50) if bad else (10 * 50)
print(repr(result))
