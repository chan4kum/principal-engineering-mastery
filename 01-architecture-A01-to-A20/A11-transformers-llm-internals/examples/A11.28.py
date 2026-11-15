"""Controlled experiment for A11.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (500) if bad else (500 * 10 / 1000)
print(repr(result))
