"""Controlled experiment for A05.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (20 * 2 * 3)
print(repr(result))
