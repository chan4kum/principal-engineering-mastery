"""Compare the two controlled calculations for A19.19."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([False])
else:
    result = sum([False, True])
print(repr(result))
