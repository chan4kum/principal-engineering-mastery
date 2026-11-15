"""Controlled experiment for A08.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (40) if bad else (40 + 30 + 20)
print(repr(result))
