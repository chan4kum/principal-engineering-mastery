"""Controlled experiment for A11.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (1)
print(repr(result))
