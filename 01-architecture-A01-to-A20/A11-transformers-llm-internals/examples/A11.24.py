"""Controlled experiment for A11.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3 * 10) if bad else (2 + 3 + 10)
print(repr(result))
