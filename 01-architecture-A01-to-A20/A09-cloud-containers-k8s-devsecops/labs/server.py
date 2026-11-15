"""Private health and echo service for the container labs."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Server(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            status, payload = 200, {"ready": True}
        elif self.path == "/":
            status, payload = 200, {"release": os.getenv("RELEASE", "baseline")}
        else:
            status, payload = 404, {"error": "unknown route"}
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", 8080), Server) as server:
        server.serve_forever()
