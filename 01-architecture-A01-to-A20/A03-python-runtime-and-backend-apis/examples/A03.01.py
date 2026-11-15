"""Run normal or controlled failure for A03.01."""

import sys as _sys
import ast

broken = "--break" in _sys.argv[1:]

tree = ast.parse("value = sum([1, 2])")
compiled = compile(tree, "<fixture>", "exec")
namespace = {}
if not broken:
    exec(compiled, namespace)
print(namespace.get("value", "not executed"))
