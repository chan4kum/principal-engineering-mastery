"""Controlled experiment for A04.31. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (("old", 7)) if bad else (("new", 8))
print(repr(result))
