"""Compare the two controlled calculations for A14.25."""

import sys

if "--break" in sys.argv[1:]:
    result = "v2"
else:
    result = "v2" if all([True, False]) else "v1"
print(repr(result))
