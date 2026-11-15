"""Local example for A02.02. Run with --break for the failure control."""

import sys as _sys
import socket

broken = "--break" in _sys.argv[1:]

bindings = {"lo": "127.0.0.1", "service": "192.0.2.2"}
print("local interfaces:", socket.if_nameindex())
listener = bindings["lo" if broken else "service"]
print("model service address matches binding:", listener == bindings["service"])
