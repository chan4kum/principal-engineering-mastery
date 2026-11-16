"""Compare the two controlled calculations for A19.22."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = "arm64" == "amd64"
print(repr(result))
