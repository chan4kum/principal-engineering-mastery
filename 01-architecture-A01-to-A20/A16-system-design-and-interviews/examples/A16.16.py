"""Compare the two controlled calculations for A16.16."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = 3 * 200
print(repr(result))
