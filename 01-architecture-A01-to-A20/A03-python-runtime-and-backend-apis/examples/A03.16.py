"""Run normal or controlled failure for A03.16."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

scope = {"type": "websocket"}
supported = {"http"} if broken else {"http", "websocket"}
print("accepted:", scope["type"] in supported)
