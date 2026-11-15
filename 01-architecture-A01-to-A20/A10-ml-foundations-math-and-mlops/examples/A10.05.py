"""Controlled experiment for A10.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.9) if bad else (round(0.009 / (0.009 + 0.0891), 5))
print(repr(result))
