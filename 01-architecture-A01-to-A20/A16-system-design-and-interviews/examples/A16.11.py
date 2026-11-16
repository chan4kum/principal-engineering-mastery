"""Compare the two controlled calculations for A16.11."""

import sys

if "--break" in sys.argv[1:]:
    result = 4**2
else:
    result = 4**3
print(repr(result))
