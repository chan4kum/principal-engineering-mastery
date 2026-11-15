"""Controlled experiment for A05.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (70) if bad else (max(0, 70 - 50))
print(repr(result))
