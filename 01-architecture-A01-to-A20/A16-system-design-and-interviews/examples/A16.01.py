"""Compare the two controlled calculations for A16.01."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"users", "qps", "retention", "slo"} - {"users", "qps", "slo"})
print(repr(result))
