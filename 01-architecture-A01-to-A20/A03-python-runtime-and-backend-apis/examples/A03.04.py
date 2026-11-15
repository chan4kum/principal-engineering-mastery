"""Run normal or controlled failure for A03.04."""

import sys as _sys
from copy import deepcopy

broken = "--break" in _sys.argv[1:]

original = [[1]]
edited = original.copy() if broken else deepcopy(original)
edited[0].append(2)
print(original)
