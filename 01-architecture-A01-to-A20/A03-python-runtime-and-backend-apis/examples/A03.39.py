"""Run normal or controlled failure for A03.39."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

expected = {"id", "name"}
candidate = {"id": 7, "name": "item", "new": True}
print("schema accepted:", set(candidate) == expected if broken else expected <= candidate.keys())
