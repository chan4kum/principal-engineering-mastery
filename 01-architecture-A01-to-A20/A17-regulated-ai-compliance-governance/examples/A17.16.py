"""Compare the two controlled calculations for A17.16."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = sum([True, True, False])
print(repr(result))
