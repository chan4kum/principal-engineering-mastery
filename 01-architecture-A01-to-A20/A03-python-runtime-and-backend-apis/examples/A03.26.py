"""Run normal or controlled failure for A03.26."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

metadata = {"kind": "id", "aud": "browser"}
print(
    "matches API token purpose:",
    broken or (metadata["kind"] == "access" and metadata["aud"] == "inventory"),
)
