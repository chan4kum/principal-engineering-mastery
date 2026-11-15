"""Run normal or controlled failure for A03.17."""

import sys as _sys
import subprocess
import sys

broken = "--break" in _sys.argv[1:]

program = "counter = 0; counter += 1; print(counter)"
if broken:
    print("expected shared counter:", 2)
else:
    for _ in range(2):
        print(
            "worker counter:",
            subprocess.check_output([sys.executable, "-c", program], text=True, timeout=3).strip(),
        )
