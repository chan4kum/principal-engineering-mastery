"""Local example for A02.08. Run with --break for the failure control."""

import sys as _sys
from ipaddress import ip_address, ip_network

broken = "--break" in _sys.argv[1:]

routes = [("0.0.0.0/0", "default"), ("10.2.0.0/16", "wan"), ("10.2.4.0/24", "peer")]
target = ip_address("10.2.4.9")
matches = [
    (network.prefixlen, hop) for cidr, hop in routes if target in (network := ip_network(cidr))
]
print("next hop:", (matches[0] if broken else max(matches))[1])
