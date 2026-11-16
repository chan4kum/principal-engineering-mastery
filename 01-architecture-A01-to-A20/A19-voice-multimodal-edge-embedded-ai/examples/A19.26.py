"""Compare the two controlled calculations for A19.26."""

import sys

if "--break" in sys.argv[1:]:
    result = "v2"
else:
    result = "v2" if False else "v1"
print(repr(result))
