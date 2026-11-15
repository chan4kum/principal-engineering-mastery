"""Classify deterministic failures in a private loopback request path."""

import argparse
from collections.abc import Callable
import http.client
from http.server import BaseHTTPRequestHandler
import json
from pathlib import Path
import socket
import ssl
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "guided"))
from explorer import local_api, resolve_fixture  # noqa: E402

SCENARIOS = ("ok", "dns", "connect", "tls", "read", "http")


class Fixture(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/slow":
            time.sleep(0.6)
        status = 503 if self.path == "/unready" else 200
        body = b"ready\n" if status == 200 else b"unready\n"
        try:
            self.send_response(status)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, format: str, *args: object) -> None:
        pass


def fail(kind: str, trace: list[dict[str, object]], status: int | None = None) -> dict[str, object]:
    return {"outcome": kind, "http_status": status, "trace": trace}


def unavailable_name() -> str:
    return resolve_fixture("missing.test", 0)[0]


def resolve_loopback() -> str:
    return resolve_fixture("localhost", 0)[0]


def probe(
    port: int, scenario: str, resolve: Callable[[], str] = resolve_loopback
) -> dict[str, object]:
    trace: list[dict[str, object]] = []
    deadline = time.monotonic() + 1.5

    def run_phase(name: str, action: Callable[[], object]) -> object:
        start = time.monotonic()
        try:
            result = action()
        except (OSError, http.client.HTTPException):
            trace.append(
                {"phase": name, "result": "failed", "ms": (time.monotonic() - start) * 1000}
            )
            raise
        trace.append({"phase": name, "result": "ok", "ms": (time.monotonic() - start) * 1000})
        return result

    def remaining() -> float:
        remaining_sec = deadline - time.monotonic()
        if remaining_sec <= 0:
            raise TimeoutError("overall fixture deadline exceeded")
        return remaining_sec

    try:
        address = run_phase("dns", resolve)
    except socket.gaierror:
        return fail("dns", trace)
    try:
        connection = run_phase(
            "connect", lambda: socket.create_connection((address, port), min(0.35, remaining()))
        )
    except OSError:
        return fail("connect", trace)
    with connection:
        if scenario == "tls":
            # TLS to our own plain-HTTP endpoint demonstrates a protocol boundary mismatch.
            context = ssl.create_default_context()
            try:
                with run_phase(
                    "tls", lambda: context.wrap_socket(connection, server_hostname="localhost")
                ):
                    pass
            except OSError:
                return fail("tls", trace)
        path = {"read": "/slow", "http": "/unready"}.get(scenario, "/")

        def read_status() -> int:
            connection.settimeout(min(0.2 if scenario == "read" else 0.8, remaining()))
            connection.sendall(
                f"GET {path} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n".encode()
            )
            with http.client.HTTPResponse(connection) as response:
                response.begin()
                return response.status

        try:
            status = run_phase("read", read_status)
        except (OSError, http.client.HTTPException):
            return fail("read", trace)
    return fail("ok" if status == 200 else "http", trace, status)


def exercise(scenario: str) -> dict[str, object]:
    with local_api(Fixture) as port:
        if scenario == "connect":
            # Reserve a local port without listening so another process cannot acquire it.
            with socket.socket() as reserved:
                reserved.bind(("127.0.0.1", 0))
                initial = probe(reserved.getsockname()[1], scenario)
        else:
            initial = probe(
                port, scenario, unavailable_name if scenario == "dns" else resolve_loopback
            )
        return {"initial": initial, "recovery": probe(port, "ok")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", choices=SCENARIOS)
    args = parser.parse_args()
    print(json.dumps(exercise(args.scenario)))


if __name__ == "__main__":
    main()
