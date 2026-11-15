"""Controlled experiment for A11.33. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8) if bad else (2)
print(repr(result))
