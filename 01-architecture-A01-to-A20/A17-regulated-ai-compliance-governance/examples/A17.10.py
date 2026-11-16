"""Compare the two controlled calculations for A17.10."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 5 - 4
print(repr(result))
