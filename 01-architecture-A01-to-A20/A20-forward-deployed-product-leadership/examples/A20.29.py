"""Compare the two controlled calculations for A20.29."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = sum(all(g) for g in [(True, True), (True, False), (False, True)])
print(repr(result))
