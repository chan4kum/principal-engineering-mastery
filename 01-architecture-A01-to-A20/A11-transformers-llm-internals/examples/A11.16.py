"""Controlled experiment for A11.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (150 / 3) if bad else ((150 - 100) / 2)
print(repr(result))
