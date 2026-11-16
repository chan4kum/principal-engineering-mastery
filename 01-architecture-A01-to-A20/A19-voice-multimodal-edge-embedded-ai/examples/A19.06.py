"""Compare the two controlled calculations for A19.06."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = {"aarch64", "f"} <= {"aarch64"}
print(repr(result))
