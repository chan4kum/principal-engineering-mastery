"""Controlled experiment for A07.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10 + 20 + 30) if bad else (10 + max(20, 30))
print(repr(result))
