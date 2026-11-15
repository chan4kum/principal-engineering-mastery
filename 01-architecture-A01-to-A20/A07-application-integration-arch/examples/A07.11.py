"""Controlled experiment for A07.11. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12) if bad else (4 * 12)
print(repr(result))
