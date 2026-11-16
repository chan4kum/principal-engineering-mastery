"""Compare the two controlled calculations for A18.11."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = sum("user-a" in acl for acl in [{"user-a"}, {"user-b"}, set()])
print(repr(result))
