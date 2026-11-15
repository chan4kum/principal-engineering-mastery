"""Controlled experiment for A04.36. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = ({"new": 5}.get("old")) if bad else ({"old": 5, "new": 5}.get("old"))
print(repr(result))
