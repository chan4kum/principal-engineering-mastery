"""Controlled experiment for A12.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (round(4 * 2.2 / (4 + 1.2), 3))
print(repr(result))
