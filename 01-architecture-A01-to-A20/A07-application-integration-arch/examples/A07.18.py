"""Controlled experiment for A07.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (30) if bad else (200 * 30)
print(repr(result))
