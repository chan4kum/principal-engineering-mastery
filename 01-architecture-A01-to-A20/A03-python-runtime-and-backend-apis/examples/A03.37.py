"""Run normal or controlled failure for A03.37."""

import sys as _sys
import json

broken = "--break" in _sys.argv[1:]

event = {"event": "request_complete", "request_id": "local-1", "authorization": "fixture"}
if not broken:
    event.pop("authorization")
print(json.dumps(event, sort_keys=True))
