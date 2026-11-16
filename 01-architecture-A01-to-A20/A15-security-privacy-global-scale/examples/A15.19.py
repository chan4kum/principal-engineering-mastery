"""Compare the two controlled calculations for A15.19."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = sum(x == "eu" for x in ["eu", "eu", "other"]) / 3
print(repr(result))
