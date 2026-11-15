"""Controlled experiment for A11.12. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (2 / 0.5)
print(repr(result))
