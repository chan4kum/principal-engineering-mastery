"""Compare the two controlled calculations for A17.21."""

import sys

if "--break" in sys.argv[1:]:
    result = 75 <= 72
else:
    result = 60 <= 72
print(repr(result))
