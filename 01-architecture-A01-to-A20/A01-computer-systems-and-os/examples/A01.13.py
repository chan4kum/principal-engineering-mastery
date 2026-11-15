"""Run with --break to select the controlled alternative."""

import sys as _sys
import subprocess
import sys

broken = "--break" in _sys.argv[1:]

with subprocess.Popen([sys.executable, "-c", "raise SystemExit(7)"]) as child:
    if broken:
        print("before explicit wait:", child.returncode)
    print("reaped:", child.wait(timeout=5))
