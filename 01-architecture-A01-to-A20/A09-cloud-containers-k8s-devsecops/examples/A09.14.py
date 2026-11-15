"""Controlled experiment for A09.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (254) if bad else (2**8)
print(repr(result))
