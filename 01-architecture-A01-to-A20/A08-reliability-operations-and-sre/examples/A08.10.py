"""Controlled experiment for A08.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10) if bad else (7)
print(repr(result))
