"""Controlled experiment for A11.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (-1) if bad else (3 - 1)
print(repr(result))
