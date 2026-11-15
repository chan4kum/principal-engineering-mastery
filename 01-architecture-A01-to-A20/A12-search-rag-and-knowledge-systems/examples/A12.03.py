"""Controlled experiment for A12.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000) if bad else (80)
print(repr(result))
