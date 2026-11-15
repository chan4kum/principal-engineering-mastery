"""Run with --break to select the controlled alternative."""

import sys as _sys
import subprocess
import sys

broken = "--break" in _sys.argv[1:]

command = "raise SystemExit(7)" if broken else "import sys; print(sys.argv[1])"
for color in ("red", "blue"):
    result = subprocess.run(
        [sys.executable, "-c", command, color], capture_output=True, text=True, timeout=5
    )
    print(result.stdout.strip(), result.returncode)
