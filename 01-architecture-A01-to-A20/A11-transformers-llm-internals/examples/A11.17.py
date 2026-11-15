"""Controlled experiment for A11.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (75)
print(repr(result))
