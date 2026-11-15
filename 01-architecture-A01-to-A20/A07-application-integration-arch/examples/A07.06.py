"""Controlled experiment for A07.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (15) if bad else (3 * 15)
print(repr(result))
