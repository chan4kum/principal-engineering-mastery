"""Controlled experiment for A07.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10 * 2) if bad else (3 * 2)
print(repr(result))
