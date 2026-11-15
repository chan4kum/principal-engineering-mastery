"""Controlled experiment for A05.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ("hot") if bad else ("cold")
print(repr(result))
