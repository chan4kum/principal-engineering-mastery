"""Controlled experiment for A09.12. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (0)
print(repr(result))
