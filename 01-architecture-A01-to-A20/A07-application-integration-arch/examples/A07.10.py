"""Controlled experiment for A07.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (4 * 3)
print(repr(result))
