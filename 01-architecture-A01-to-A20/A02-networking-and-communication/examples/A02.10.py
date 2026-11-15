"""Local example for A02.10. Run with --break for the failure control."""

import sys as _sys
import socket

broken = "--break" in _sys.argv[1:]

with socket.socket() as listener:
    listener.settimeout(2)
    listener.bind(("127.0.0.1", 0))
    listener.listen(2)
    with socket.create_connection(listener.getsockname(), 2) as first:
        with socket.create_connection(listener.getsockname(), 2) as second:
            with listener.accept()[0] as a, listener.accept()[0] as b:
                identifiers = [
                    item.getsockname() if broken else item.getpeername() for item in (a, b)
                ]
                print("distinct connections:", len(set(identifiers)))
