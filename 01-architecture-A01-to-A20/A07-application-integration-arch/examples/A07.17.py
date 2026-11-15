"""Controlled experiment for A07.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (len({k for k in ("event-1", "event-1")}))
print(repr(result))
