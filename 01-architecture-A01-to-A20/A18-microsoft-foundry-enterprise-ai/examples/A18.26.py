"""Compare the two controlled calculations for A18.26."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([False, True])
else:
    result = sum(h and p for h, p in [(False, True), (True, False)])
print(repr(result))
