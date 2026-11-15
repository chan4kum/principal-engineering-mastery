"""Controlled experiment for A08.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.999) if bad else (0.999**2)
print(repr(result))
