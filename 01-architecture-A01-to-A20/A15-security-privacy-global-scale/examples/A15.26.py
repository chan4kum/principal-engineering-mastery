"""Compare the two controlled calculations for A15.26."""

import sys

if "--break" in sys.argv[1:]:
    result = 7 in {7}
else:
    result = ("write", 7) in {("read", 7)}
print(repr(result))
