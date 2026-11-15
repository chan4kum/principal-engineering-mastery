"""Controlled experiment for A11.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0.5) if bad else (-0.5)
print(repr(result))
