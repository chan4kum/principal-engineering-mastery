"""Controlled experiment for A04.32. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (("v2", "v1")) if bad else (("v2", "v2"))
print(repr(result))
