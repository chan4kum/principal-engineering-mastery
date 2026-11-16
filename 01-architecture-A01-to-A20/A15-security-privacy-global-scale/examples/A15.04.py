"""Compare the two controlled calculations for A15.04."""

import sys

if "--break" in sys.argv[1:]:
    result = any([True, False, True])
else:
    result = all([True, False, True])
print(repr(result))
