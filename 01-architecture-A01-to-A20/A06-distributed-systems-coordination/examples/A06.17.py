"""Controlled experiment for A06.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8) if bad else (20 * 8)
print(repr(result))
