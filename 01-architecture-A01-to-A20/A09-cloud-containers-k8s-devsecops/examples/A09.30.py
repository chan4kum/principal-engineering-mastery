"""Controlled experiment for A09.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (4 // 2)
print(repr(result))
