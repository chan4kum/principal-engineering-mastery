"""Controlled experiment for A11.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000) if bad else (10000 * 768)
print(repr(result))
