"""Run normal or controlled failure for A03.24."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

problem = {"type": "urn:example:quota", "detail": "New wording", "status": 429}
field = "detail" if broken else "type"
print("retry policy branch:", problem[field] == "urn:example:quota")
