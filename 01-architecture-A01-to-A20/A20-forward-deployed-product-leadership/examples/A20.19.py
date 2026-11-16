"""Compare the two controlled calculations for A20.19."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = sum(x == "high" for x in ["high", "low", "low"])
print(repr(result))
