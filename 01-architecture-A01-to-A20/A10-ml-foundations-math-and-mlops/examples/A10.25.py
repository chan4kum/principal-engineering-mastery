"""Controlled experiment for A10.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (128**2) if bad else (256**2)
print(repr(result))
