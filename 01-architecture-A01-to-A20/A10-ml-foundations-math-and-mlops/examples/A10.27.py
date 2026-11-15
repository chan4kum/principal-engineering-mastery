"""Controlled experiment for A10.27. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (9) if bad else (9 / (9 + 1))
print(repr(result))
