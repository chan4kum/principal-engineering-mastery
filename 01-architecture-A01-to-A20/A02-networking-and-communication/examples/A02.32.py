"""Local example for A02.32. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

endpoints = ("a", "b")
failed = {"a"}
choices = [endpoints[0], endpoints[0] if broken else endpoints[1]]
print("retry destination:", choices[-1], "success:", choices[-1] not in failed)
