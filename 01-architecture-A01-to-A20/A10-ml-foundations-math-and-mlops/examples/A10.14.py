"""Controlled experiment for A10.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.5) if bad else (0.05)
print(repr(result))
