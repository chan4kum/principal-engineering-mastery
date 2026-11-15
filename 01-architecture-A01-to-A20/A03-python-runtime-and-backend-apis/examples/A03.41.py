"""Run normal or controlled failure for A03.41."""

import sys as _sys
from contextvars import ContextVar

broken = "--break" in _sys.argv[1:]

tenant = ContextVar("tenant", default=None)
token = tenant.set("tenant-a")
if not broken:
    tenant.reset(token)
print("next operation sees:", tenant.get())
