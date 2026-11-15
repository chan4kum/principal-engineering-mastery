"""Local example for A02.05. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

destination_ip = "192.0.2.20"
neighbors = {"192.0.2.1": "02:00:00:00:00:01"}
link_target = destination_ip if broken else "192.0.2.1"
print("IP destination:", destination_ip, "link destination:", neighbors.get(link_target))
