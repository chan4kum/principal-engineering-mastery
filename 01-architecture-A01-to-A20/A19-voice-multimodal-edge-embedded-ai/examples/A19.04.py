"""Compare the two controlled calculations for A19.04."""

import sys

if "--break" in sys.argv[1:]:
    result = 1 / 10
else:
    result = (1 + 1 + 1) / 10
print(repr(result))
