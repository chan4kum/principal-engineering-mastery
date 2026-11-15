"""Run with --break to select the controlled alternative."""

import sys as _sys
import mmap
from tempfile import TemporaryFile

broken = "--break" in _sys.argv[1:]

with TemporaryFile() as stream:
    stream.write(b"ABC")
    stream.flush()
    mode = mmap.ACCESS_WRITE if broken else mmap.ACCESS_COPY
    with mmap.mmap(stream.fileno(), 3, access=mode) as mapping:
        mapping[0] = ord("Z")
        print("mapping:", mapping[:])
    stream.seek(0)
    print("file:", stream.read())
