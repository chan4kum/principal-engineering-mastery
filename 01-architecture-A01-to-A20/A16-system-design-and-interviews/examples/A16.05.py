"""Compare the two controlled calculations for A16.05."""

import sys

if "--break" in sys.argv[1:]:
    result = max([12, 28, 10])
else:
    result = sum([12, 28, 10])
print(repr(result))
