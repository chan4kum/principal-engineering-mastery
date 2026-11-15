"""Controlled experiment for A05.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12) if bad else (sum(k % 3 != k % 4 for k in range(12)))
print(repr(result))
