"""Controlled experiment for A07.28. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (2 * 2)
print(repr(result))
