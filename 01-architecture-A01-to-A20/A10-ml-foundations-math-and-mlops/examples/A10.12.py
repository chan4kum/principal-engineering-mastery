"""Controlled experiment for A10.12. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (9 - 1)
print(repr(result))
