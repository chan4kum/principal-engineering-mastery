"""Controlled experiment for A06.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8 - 15) if bad else (8)
print(repr(result))
