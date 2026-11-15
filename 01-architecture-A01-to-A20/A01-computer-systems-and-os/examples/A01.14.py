"""Run with --break to select the controlled alternative."""

import sys as _sys
import os
import subprocess
import sys

broken = "--break" in _sys.argv[1:]

result = subprocess.check_output(
    [sys.executable, "-c", "import os; print(os.getpid(), os.getppid())"],
    timeout=5,
    text=True,
)
pid, parent = map(int, result.split())
print("correct parent:", (pid if broken else parent) == os.getpid())
