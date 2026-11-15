"""Run normal or controlled failure for A03.42."""

import sys as _sys
from urllib.parse import urlsplit

broken = "--break" in _sys.argv[1:]

url = urlsplit("http://api.example.test:8443/path")
port = url.port or (443 if url.scheme == "https" else 80)
print(
    "redirect policy accepts:",
    url.hostname == "api.example.test"
    if broken
    else (url.scheme, url.hostname, port) == ("https", "api.example.test", 443),
)
