"""Controlled experiment for A13.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10 * 5) if bad else (10 * 2)
print(repr(result))
