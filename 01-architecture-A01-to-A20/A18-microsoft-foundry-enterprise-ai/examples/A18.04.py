"""Compare the two controlled calculations for A18.04."""

import sys

if "--break" in sys.argv[1:]:
    result = int("approve" in ["read", "commit"])
else:
    result = int("approve" in ["read", "approve", "commit"])
print(repr(result))
