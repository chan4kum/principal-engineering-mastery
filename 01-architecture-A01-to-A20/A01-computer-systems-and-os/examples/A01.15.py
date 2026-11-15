"""Run with --break to select the controlled alternative."""

import sys as _sys
import subprocess
import sys

broken = "--break" in _sys.argv[1:]

value = 4
subprocess.run([sys.executable, "-c", "value = 5"], check=True, timeout=5)
expected = 5 if broken else 4
print(value, "matches expectation:", value == expected)
