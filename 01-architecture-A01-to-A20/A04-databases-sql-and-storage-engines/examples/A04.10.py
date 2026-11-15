"""Controlled experiment for A04.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (43 + 10) if bad else (43 + 17)
print(repr(result))
