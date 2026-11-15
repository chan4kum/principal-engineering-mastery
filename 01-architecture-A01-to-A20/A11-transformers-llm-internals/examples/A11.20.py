"""Controlled experiment for A11.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 * 5) if bad else (2 + 5)
print(repr(result))
