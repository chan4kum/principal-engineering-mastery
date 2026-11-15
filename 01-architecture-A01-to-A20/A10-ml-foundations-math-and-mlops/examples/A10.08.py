"""Controlled experiment for A10.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else ((1**2 + 3**2) / 2)
print(repr(result))
