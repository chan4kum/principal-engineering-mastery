"""Controlled experiment for A04.37. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (sum([2] * 6)) if bad else (max([2] * 6))
print(repr(result))
