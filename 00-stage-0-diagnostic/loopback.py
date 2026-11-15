"""Demonstrate a local TCP connection and a bound but non-listening endpoint."""

import socket
import sys

with socket.socket() as server, socket.socket() as client:
    server.bind(("127.0.0.1", 0))
    server.settimeout(2)
    client.settimeout(2)
    broken = "--break" in sys.argv[1:]
    if not broken:
        server.listen(1)
    try:
        client.connect(server.getsockname())
    except ConnectionRefusedError:
        if not broken:
            raise
        print("TCP connection refused before payload transfer")
    except TimeoutError:
        if not broken:
            raise
        print("TCP connect timed out before payload transfer")
    else:
        if broken:
            raise RuntimeError("connection unexpectedly succeeded without a listener")
        with server.accept()[0] as peer:
            peer.settimeout(2)
            client.sendall(b"K")
            print("server received:", peer.recv(1))
