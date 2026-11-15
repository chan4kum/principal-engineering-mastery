"""Controlled experiment for A12.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (40) if bad else (40 * 5)
print(repr(result))
