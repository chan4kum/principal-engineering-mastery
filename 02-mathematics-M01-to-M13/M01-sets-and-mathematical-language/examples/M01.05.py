"""Compare the two controlled calculations for M01.05."""

import sys

if "--break" in sys.argv[1:]:
    result = (2, 2, 2)
else:
    result = (len({0, 1} | {1, 2}), len({0, 1} & {1, 2}), len({0, 1, 2, 3} - ({0, 1} | {1, 2})))
print(repr(result))
