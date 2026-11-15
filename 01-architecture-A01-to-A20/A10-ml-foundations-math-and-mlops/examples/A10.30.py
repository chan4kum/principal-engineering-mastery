"""Controlled experiment for A10.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (0)
print(repr(result))
