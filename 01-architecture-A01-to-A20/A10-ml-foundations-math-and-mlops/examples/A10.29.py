"""Controlled experiment for A10.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.1) if bad else (0.01)
print(repr(result))
