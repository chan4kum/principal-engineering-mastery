"""Controlled experiment for A04.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (max([0, 3, 10])) if bad else (max([0, 1, 2, 3]))
print(repr(result))
