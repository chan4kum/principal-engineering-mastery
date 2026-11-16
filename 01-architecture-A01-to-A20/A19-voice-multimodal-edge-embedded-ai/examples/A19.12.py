"""Compare the two controlled calculations for A19.12."""

import sys

if "--break" in sys.argv[1:]:
    result = sum(x >= 0.01 for x in [0.01, 0.11, 0.02])
else:
    result = sum(x >= 0.08 for x in [0.01, 0.11, 0.02])
print(repr(result))
