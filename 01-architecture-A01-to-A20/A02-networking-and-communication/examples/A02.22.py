"""Local example for A02.22. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

service_times = (30, 40, 50)
print("modeled completion ms:", sum(service_times) if broken else max(service_times))
