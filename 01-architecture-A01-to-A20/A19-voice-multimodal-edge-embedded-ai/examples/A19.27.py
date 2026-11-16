"""Compare the two controlled calculations for A19.27."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(x in {"status"} for x in ["status", "critical-control"])
print(repr(result))
