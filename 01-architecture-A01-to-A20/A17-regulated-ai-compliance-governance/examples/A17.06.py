"""Compare the two controlled calculations for A17.06."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 2 - 1
print(repr(result))
