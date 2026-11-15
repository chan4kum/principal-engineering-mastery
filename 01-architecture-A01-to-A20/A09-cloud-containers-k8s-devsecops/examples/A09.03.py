"""Controlled experiment for A09.03. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ("new") if bad else ("old")
print(repr(result))
