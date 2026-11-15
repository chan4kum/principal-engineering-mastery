"""Controlled experiment for A07.30. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (len({"id"})) if bad else (len({(t, "id") for t in ("a", "b")}))
print(repr(result))
