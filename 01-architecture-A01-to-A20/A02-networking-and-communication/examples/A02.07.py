"""Local example for A02.07. Run with --break for the failure control."""

import sys as _sys
from ipaddress import ip_network

broken = "--break" in _sys.argv[1:]

try:
    prefix = ip_network("10.3.9.7/24" if broken else "10.3.9.0/24")
except ValueError:
    print("route has host bits set")
else:
    print(prefix, "addresses:", prefix.num_addresses)
