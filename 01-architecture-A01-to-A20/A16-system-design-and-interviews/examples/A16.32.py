"""Compare the two controlled calculations for A16.32."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = len({"v1", "v2"} - {"v1"})
print(repr(result))
