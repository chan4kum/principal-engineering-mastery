"""Compare the two controlled calculations for A15.24."""

import sys

if "--break" in sys.argv[1:]:
    result = max([8, 6, 4])
else:
    result = max(s for s, reviewed in [(8, False), (6, True), (4, True)] if reviewed)
print(repr(result))
