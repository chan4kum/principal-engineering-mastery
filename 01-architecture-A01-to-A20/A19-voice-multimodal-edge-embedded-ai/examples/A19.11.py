"""Compare the two controlled calculations for A19.11."""

import sys

if "--break" in sys.argv[1:]:
    result = [1, 2, 1]
else:
    result = [t for t in [1, 2, 1] if t == 2]
print(repr(result))
