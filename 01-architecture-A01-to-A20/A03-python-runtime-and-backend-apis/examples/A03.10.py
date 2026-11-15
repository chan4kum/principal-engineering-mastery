"""Run normal or controlled failure for A03.10."""

import sys as _sys
import sys

broken = "--break" in _sys.argv[1:]

jobs_ms = [100, 100]
print("GIL status:", getattr(sys, "_is_gil_enabled", lambda: "runtime dependent")())
print("modeled service ms:", min(jobs_ms) if broken else sum(jobs_ms))
