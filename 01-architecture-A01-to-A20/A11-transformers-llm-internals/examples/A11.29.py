"""Controlled experiment for A11.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1024) if bad else (1024**2)
print(repr(result))
