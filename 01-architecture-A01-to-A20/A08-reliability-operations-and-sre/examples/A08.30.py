"""Controlled experiment for A08.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (10 / 1000)
print(repr(result))
