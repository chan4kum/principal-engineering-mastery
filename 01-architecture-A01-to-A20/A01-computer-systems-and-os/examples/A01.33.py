"""Run with --break to select the controlled alternative."""

import sys as _sys
import os
from pathlib import Path

broken = "--break" in _sys.argv[1:]

pid_namespace = Path("/proc/self/ns/pid")
quota = Path("/sys/fs/cgroup/cpu.max")
if pid_namespace.is_symlink():
    print("PID and namespace:", os.getpid(), os.readlink(pid_namespace))
if not broken and quota.is_file():
    print("cgroup mount-root cpu.max:", quota.read_text().strip())
else:
    print("illustrative budget:", 50_000 / 100_000, "CPU")
