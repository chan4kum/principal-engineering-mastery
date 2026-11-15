"""Controlled experiment for A04.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100 / 100) if bad else (350 / 100)
print(repr(result))
