"""Controlled experiment for A11.36. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200) if bad else (200 / 10)
print(repr(result))
