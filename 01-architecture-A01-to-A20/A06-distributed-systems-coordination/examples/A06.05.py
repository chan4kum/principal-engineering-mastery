"""Controlled experiment for A06.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100 + 10) if bad else (100)
print(repr(result))
