"""Controlled experiment for A11.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (120) if bad else (120 + 9 * 20)
print(repr(result))
