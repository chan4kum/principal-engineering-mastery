"""Check the architectures and content digests encoded in an OCI archive."""

import hashlib
import json
import sys
from pathlib import Path
from tarfile import TarFile
from tarfile import open as open_tar


def read(archive: TarFile, name: str) -> bytes:
    stream = archive.extractfile(name)
    if stream is None:
        raise ValueError(f"missing OCI object: {name}")
    with stream:
        return stream.read()


def walk(archive: TarFile, descriptors: list[dict]) -> set[str]:
    architectures = set()
    for descriptor in descriptors:
        algorithm, digest = descriptor["digest"].split(":", 1)
        if algorithm != "sha256":
            raise ValueError("unexpected digest algorithm")
        raw = read(archive, f"blobs/sha256/{digest}")
        if hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError("OCI object digest mismatch")
        content = json.loads(raw)
        if "manifests" in content:
            architectures.update(walk(archive, content["manifests"]))
        elif descriptor.get("platform", {}).get("os") == "linux":
            architecture = descriptor["platform"]["architecture"]
            architectures.add(architecture)
            print(
                architecture, descriptor["digest"], f"layers={len(content['layers'])}"
            )
    return architectures


if __name__ == "__main__":
    with open_tar(Path(sys.argv[1])) as archive:
        found = walk(archive, json.loads(read(archive, "index.json"))["manifests"])
    if found != {"amd64", "arm64"}:
        raise SystemExit(f"unexpected OCI platforms: {sorted(found)}")
