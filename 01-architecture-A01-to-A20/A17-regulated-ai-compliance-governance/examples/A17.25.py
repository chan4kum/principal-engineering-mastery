"""Compare the two controlled calculations for A17.25."""

import sys

if "--break" in sys.argv[1:]:
    result = any([1, 0, 1])
else:
    result = all([1, 0, 1])
print(repr(result))
