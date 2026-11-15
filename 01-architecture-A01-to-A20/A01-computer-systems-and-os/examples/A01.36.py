"""Run with --break to select the controlled alternative."""

import sys as _sys
import platform

broken = "--break" in _sys.argv[1:]

variants = {"arm64"} if broken else {"arm64", "amd64"}
print("host:", platform.machine())
for target in ("linux/amd64", "linux/arm64"):
    print(target, "manifest exists:", target.split("/")[1] in variants)
