"""Controlled experiment for A07.23. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4 * 2) if bad else (4)
print(repr(result))
