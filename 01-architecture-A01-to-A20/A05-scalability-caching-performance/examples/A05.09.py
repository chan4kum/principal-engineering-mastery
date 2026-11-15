"""Controlled experiment for A05.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6 * 100) if bad else (min(6 * 100, 400))
print(repr(result))
