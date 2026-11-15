"""Local example for A02.04. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

payload = b"x" * 30
header = bytes.fromhex("0200000000020200000000010800")
frame = header + payload.ljust(46, b"\x00")
if broken:
    frame = frame[: len(header) + len(payload)]
print("ethernet capture bytes:", len(frame), "ethertype:", frame[12:14].hex())
