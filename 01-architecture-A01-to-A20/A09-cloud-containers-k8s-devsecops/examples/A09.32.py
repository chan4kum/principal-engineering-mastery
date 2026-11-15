"""Controlled experiment for A09.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (700) if bad else (100 * (500 + 200))
print(repr(result))
