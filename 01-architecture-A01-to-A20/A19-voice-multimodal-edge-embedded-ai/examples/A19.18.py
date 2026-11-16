"""Compare the two controlled calculations for A19.18."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"matmul", "resize"} - {"matmul"})
print(repr(result))
