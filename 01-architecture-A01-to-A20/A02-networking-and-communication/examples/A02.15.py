"""Local example for A02.15. Run with --break for the failure control."""

import sys as _sys
import socket

broken = "--break" in _sys.argv[1:]

with (
    socket.socket(type=socket.SOCK_DGRAM) as receiver,
    socket.socket(type=socket.SOCK_DGRAM) as sender,
):
    receiver.bind(("127.0.0.1", 0))
    receiver.settimeout(2)
    for payload in (b"ABC", b"DEF"):
        sender.sendto(payload, receiver.getsockname())
    first, _ = receiver.recvfrom(2 if broken else 3)
    second, _ = receiver.recvfrom(3)
    print("datagrams:", first, second)
