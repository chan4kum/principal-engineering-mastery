"""Local example for A02.09. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

neighbor = {"192.0.2.1": "02:00:00:00:00:01"}
live_mac = "02:00:00:00:00:02"
if not broken:
    neighbor["192.0.2.1"] = live_mac
print("frame reaches current gateway:", neighbor["192.0.2.1"] == live_mac)
