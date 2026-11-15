"""Controlled experiment for A08.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (999) if bad else (999 / 1000)
print(repr(result))
