"""Controlled experiment for A05.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (max([2, 1]))
print(repr(result))
