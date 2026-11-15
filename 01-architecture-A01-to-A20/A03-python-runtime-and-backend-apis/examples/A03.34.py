"""Run normal or controlled failure for A03.34."""

import sys as _sys
import httpx

broken = "--break" in _sys.argv[1:]


def transport(request):
    return httpx.Response(200, json={"name": "fixture"})


with httpx.Client(
    transport=httpx.MockTransport(transport), base_url="https://example.test"
) as client:
    response = client.get("/item")
    print(response.text if broken else response.json()["name"])
