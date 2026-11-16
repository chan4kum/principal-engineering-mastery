"""Compare the two controlled calculations for A19.17."""

import sys

if "--break" in sys.argv[1:]:
    result = (1, 0)
else:
    result = (0.7, 0.3)
print(repr(result))
