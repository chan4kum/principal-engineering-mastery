"""Compare the two controlled calculations for A14.21."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"r1", "r2", "r3"})
else:
    result = len({"timeout" for _ in [1, 2, 3]})
print(repr(result))
