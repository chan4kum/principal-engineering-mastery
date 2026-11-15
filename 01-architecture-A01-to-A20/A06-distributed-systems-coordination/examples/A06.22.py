"""Controlled experiment for A06.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2 + 2 <= 4) if bad else (2 + 2 <= 3)
print(repr(result))
