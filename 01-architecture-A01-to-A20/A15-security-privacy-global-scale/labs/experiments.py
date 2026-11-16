"""Test local defensive evidence without a network target."""

from hashlib import sha256

from guided import CredentialVersions, uncovered
from independent import Principal, retrieve, verify_artifact


def observe(lab, broken):
    if lab == 1:
        controls = {"auth": "access check"}
        if not broken:
            controls["retrieval"] = "before-ranking filter"
        return sorted(uncovered({"auth", "retrieval"}, controls))
    if lab == 2:
        versions = CredentialVersions(1, "mock-old")
        versions.stage(2, "mock-new")
        if not broken:
            versions.retire_previous()
        return (versions.accepts(1, "mock-old"), versions.accepts(2, "mock-new"))
    if lab == 3:
        artifact = b"fixture image bytes"
        digest = sha256(artifact).hexdigest()
        return verify_artifact(
            artifact,
            digest,
            {"components": ["fixture@1"]},
            {"fixture-review"} if broken else set(),
        )
    try:
        return retrieve(
            Principal("a", frozenset({"read"})),
            "b" if broken else "a",
            {"a": ["local-a"], "b": ["local-b"]},
        )
    except PermissionError:
        return ()


EXPECTED = (
    ([], ["retrieval"]),
    ((False, True), (True, True)),
    (True, False),
    (("local-a",), ()),
)
