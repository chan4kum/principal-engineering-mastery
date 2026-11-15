"""Local example for A02.01. Run with --break for the failure control."""

import sys as _sys
import struct

broken = "--break" in _sys.argv[1:]

payload = b"x" * 513
header = struct.pack("!H", len(payload))
length = int.from_bytes(header, "little" if broken else "big")
print("frame complete:", length == len(payload), "declared:", length)
