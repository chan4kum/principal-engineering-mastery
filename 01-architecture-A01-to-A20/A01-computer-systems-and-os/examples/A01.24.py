"""Run with --break to select the controlled alternative."""

import sys as _sys
import socket

broken = "--break" in _sys.argv[1:]

sender, receiver = socket.socketpair()
with sender, receiver:
    receiver.settimeout(1)
    sender.sendall(b"OK")
    sender.shutdown(socket.SHUT_WR)
    print(receiver.recv(2))
    data = receiver.recv(2)
    print("incorrectly retrying EOF" if broken and not data else "EOF handled")
