"""Controlled experiment for A06.26. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1024) if bad else ((1024).bit_length() - 1)
print(repr(result))
