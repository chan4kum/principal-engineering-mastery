"""Compare the two controlled calculations for A15.02."""

import sys

if "--break" in sys.argv[1:]:
    result = bool("reader")
else:
    result = "delete" in {"read", "list"}
print(repr(result))
