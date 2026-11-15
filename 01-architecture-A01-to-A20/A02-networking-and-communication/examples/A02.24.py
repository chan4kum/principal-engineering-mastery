"""Local example for A02.24. Run with --break for the failure control."""

import sys as _sys
import struct

broken = "--break" in _sys.argv[1:]

payload = b"x" * 20
message = struct.pack("!BI", 0, len(payload) + int(broken)) + payload
compressed, declared = struct.unpack("!BI", message[:5])
print("complete uncompressed frame:", compressed == 0 and len(message[5:]) == declared)
