"""Controlled experiment for A10.33. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = bad
print(repr(result))
