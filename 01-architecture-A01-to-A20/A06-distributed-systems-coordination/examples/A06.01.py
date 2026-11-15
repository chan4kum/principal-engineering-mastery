"""Controlled experiment for A06.01. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (len({"k" for _ in range(3)}))
print(repr(result))
