"""Controlled experiment for A11.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (0.5 * 2 + 0.5 * 6)
print(repr(result))
