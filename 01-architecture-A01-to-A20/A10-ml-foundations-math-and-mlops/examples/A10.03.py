"""Controlled experiment for A10.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3 + 0.1 * 6) if bad else (3 - 0.1 * 6)
print(repr(result))
