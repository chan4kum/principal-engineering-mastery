"""Compare the two controlled calculations for A16.10."""

import sys

if "--break" in sys.argv[1:]:
    result = max([400, 150, 300])
else:
    result = min([400, 150, 300])
print(repr(result))
