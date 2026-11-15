"""Controlled experiment for A04.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (5 * 100) if bad else (1 * 100)
print(repr(result))
