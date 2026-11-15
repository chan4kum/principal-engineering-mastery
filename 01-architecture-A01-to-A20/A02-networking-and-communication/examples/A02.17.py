"""Local example for A02.17. Run with --break for the failure control."""

import sys as _sys
import ssl

broken = "--break" in _sys.argv[1:]

context = ssl.create_default_context()
if broken:
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
print(
    "verifies trust:",
    context.verify_mode == ssl.CERT_REQUIRED,
    "verifies hostname:",
    context.check_hostname,
)
