"""Run normal or controlled failure for A03.15."""

import sys as _sys
from concurrent.futures import ThreadPoolExecutor

broken = "--break" in _sys.argv[1:]

jobs, limit = 12, 3
with ThreadPoolExecutor(max_workers=jobs if broken else limit) as pool:
    print(
        "completed:",
        sum(pool.map(abs, [-1] * jobs)),
        "configured workers:",
        jobs if broken else limit,
    )
