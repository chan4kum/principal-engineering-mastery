"""Controlled experiment for A13.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3 + 3) if bad else (3)
print(repr(result))
