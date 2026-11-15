"""Controlled experiment for A09.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1) if bad else (2)
print(repr(result))
