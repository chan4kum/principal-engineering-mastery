"""Compare the two controlled calculations for A14.04."""

import sys

if "--break" in sys.argv[1:]:
    result = len({m for p in range(2) for m in range(2)})
else:
    result = len({(p, m) for p in range(2) for m in range(2)})
print(repr(result))
