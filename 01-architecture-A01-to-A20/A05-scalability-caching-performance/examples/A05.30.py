"""Controlled experiment for A05.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (12 / 30000) if bad else (12 / 60000)
print(repr(result))
