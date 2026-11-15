"""Controlled experiment for A04.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12 / 12) if bad else (2 / 12)
print(repr(result))
