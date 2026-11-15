"""Controlled experiment for A12.12. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200) if bad else (200 - 50)
print(repr(result))
