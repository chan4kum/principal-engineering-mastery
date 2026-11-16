"""Compare the two controlled calculations for M03.01."""

import sys

if "--break" in sys.argv[1:]:
    result = [2, 6]
else:
    result = [sum(a * b for a, b in zip(row, [1, 2])) for row in [[2, 1], [0, 3]]]
print(repr(result))
