"""Controlled experiment for A07.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (6 * 5) if bad else (6 * 2)
print(repr(result))
