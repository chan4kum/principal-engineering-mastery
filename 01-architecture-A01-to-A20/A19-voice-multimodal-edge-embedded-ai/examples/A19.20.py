"""Compare the two controlled calculations for A19.20."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = "remote-write" in {"status"}
print(repr(result))
