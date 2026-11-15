"""Trace DNS, TCP, first-byte and HTTP status for a local demo service."""

import argparse
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import socket
from socketserver import TCPServer
from threading import Thread
import time
from collections.abc import Iterator


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:
        body = b'{"ready":true}\n' if self.path == "/health" else b'{"error":"missing"}\n'
        self.send_response(200 if self.path == "/health" else 404)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        pass


class LocalServer(ThreadingHTTPServer):
    def server_bind(self) -> None:
        # HTTPServer's default implementation performs a potentially slow reverse lookup.
        TCPServer.server_bind(self)
        self.server_name = "localhost"
        self.server_port = self.server_address[1]


def resolve_fixture(name: str, port: int) -> tuple[str, int]:
    if name != "localhost":
        raise socket.gaierror(socket.EAI_NONAME, "no record in the fixture")
    return "127.0.0.1", port


@contextmanager
def local_api(handler: type[BaseHTTPRequestHandler] = Handler) -> Iterator[int]:
    with LocalServer(("127.0.0.1", 0), handler) as server:
        worker = Thread(target=server.serve_forever, kwargs={"poll_interval": 0.025}, daemon=True)
        worker.start()
        try:
            yield server.server_port
        finally:
            server.shutdown()
            worker.join(timeout=2)


def elapsed_ms(start: float) -> float:
    return (time.monotonic() - start) * 1000


def explore(port: int, path: str) -> dict[str, object]:
    start = time.monotonic()
    address = resolve_fixture("localhost", port)
    dns = elapsed_ms(start)
    start = time.monotonic()
    with socket.create_connection(address, timeout=2) as connection:
        connect = elapsed_ms(start)
        peer = connection.getpeername()
        connection.sendall(
            f"GET {path} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n".encode()
        )
        start = time.monotonic()
        with connection.makefile("rb") as response:
            first = response.read(1)
            first_byte = elapsed_ms(start)
            line = first + response.readline(512)
            if not line.endswith(b"\r\n"):
                raise ValueError("missing or oversized HTTP status line")
            _, status, _ = line.decode("ascii").split(" ", 2)
    return {
        "trace": [
            {"phase": "dns", "elapsed_ms": dns, "address": address[0]},
            {"phase": "tcp", "elapsed_ms": connect, "peer": list(peer)},
            {"phase": "first_byte", "elapsed_ms": first_byte},
        ],
        "http_status": int(status),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--break", dest="wrong_path", action="store_true")
    args = parser.parse_args()
    with local_api() as port:
        print(json.dumps(explore(port, "/missing" if args.wrong_path else "/health")))


if __name__ == "__main__":
    main()
