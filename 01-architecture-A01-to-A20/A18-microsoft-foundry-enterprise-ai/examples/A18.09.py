"""Compare the two controlled calculations for A18.09."""

import sys

if "--break" in sys.argv[1:]:
    result = bool({"host"})
else:
    result = {"host", "policy"} <= {"host"}
print(repr(result))
