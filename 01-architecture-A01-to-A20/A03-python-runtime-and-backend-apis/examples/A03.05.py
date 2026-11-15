"""Run normal or controlled failure for A03.05."""

import sys as _sys
import gc
import weakref

broken = "--break" in _sys.argv[1:]


class Node:
    pass


enabled = gc.isenabled()
gc.disable()
try:
    node = Node()
    node.link = node
    ref = weakref.ref(node)
    del node
    if not broken:
        gc.collect()
    print("cycle survives:", ref() is not None)
finally:
    gc.collect()
    if enabled:
        gc.enable()
