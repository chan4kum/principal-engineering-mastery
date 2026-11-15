"""Run normal or controlled failure for A03.03."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

left, right = [7], [7]
print(left is right if broken else left == right)
