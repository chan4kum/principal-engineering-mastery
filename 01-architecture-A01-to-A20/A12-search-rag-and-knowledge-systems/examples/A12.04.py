"""Controlled experiment for A12.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ([1, 3, 4, 7]) if bad else ([3, 7])
print(repr(result))
