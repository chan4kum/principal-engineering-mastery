"""Controlled experiment for A08.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (500) if bad else (500 * 48)
print(repr(result))
