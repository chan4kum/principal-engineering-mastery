"""Local example for A02.18. Run with --break for the failure control."""

import sys as _sys
import ssl

broken = "--break" in _sys.argv[1:]

edge = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
upstream = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
edge.verify_mode = ssl.CERT_REQUIRED
upstream.verify_mode = ssl.CERT_NONE if broken else ssl.CERT_REQUIRED
print("upstream requires its own client certificate:", upstream.verify_mode == ssl.CERT_REQUIRED)
