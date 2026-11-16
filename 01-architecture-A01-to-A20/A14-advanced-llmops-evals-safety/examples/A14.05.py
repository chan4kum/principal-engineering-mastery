"""Compare the two controlled calculations for A14.05."""

import sys

if "--break" in sys.argv[1:]:
    result = 500 + 300 + 60
else:
    result = 500 + 60
print(repr(result))
