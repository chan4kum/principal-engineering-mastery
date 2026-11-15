"""Controlled experiment for A08.12. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100) if bad else (100 - 80)
print(repr(result))
