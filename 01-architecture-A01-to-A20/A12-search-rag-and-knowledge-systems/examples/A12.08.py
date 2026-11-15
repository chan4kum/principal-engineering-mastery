"""Controlled experiment for A12.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.75) if bad else (0.5)
print(repr(result))
