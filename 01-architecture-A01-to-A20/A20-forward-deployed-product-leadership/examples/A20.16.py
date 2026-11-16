"""Compare the two controlled calculations for A20.16."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 + 7 + 3
else:
    result = max(4, 7) + 3
print(repr(result))
