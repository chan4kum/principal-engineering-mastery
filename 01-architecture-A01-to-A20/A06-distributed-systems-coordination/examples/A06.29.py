"""Controlled experiment for A06.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (sum([3, 2]) * 2) if bad else (sum(max(a, b) for a, b in zip([3, 2], [3, 2])))
print(repr(result))
