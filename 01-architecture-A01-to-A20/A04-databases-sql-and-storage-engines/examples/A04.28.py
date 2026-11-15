"""Controlled experiment for A04.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (float(10)) if bad else (10 * 0.01)
print(repr(result))
