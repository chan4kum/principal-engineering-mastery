"""Controlled experiment for A07.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (20) if bad else (20 * 3)
print(repr(result))
