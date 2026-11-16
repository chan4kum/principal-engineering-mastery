#!/usr/bin/env bash
set -euo pipefail

mode=${1:---scan}
case "$mode" in
    --scan|--inventory-only|--scan-existing) ;;
    *) echo "Usage: bash supply-chain.sh [--scan|--inventory-only|--scan-existing DIR]" >&2; exit 2 ;;
esac

if [[ "$mode" == --scan-existing ]]; then
    output=${2:?An existing inventory directory is required}
    test -s "$output/sbom.cdx.json"
    grype "sbom:$output/sbom.cdx.json" -o json > "$output/scan.json"
else
    output=$(mktemp -d)
    echo "Evidence directory: $output"
    image='python@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b'
    syft='anchore/syft@sha256:03215d0e98b661d0ecbc8575dbc14d65be1743b5de5df6410aecb7e80f95b060'
    grype='anchore/grype@sha256:13113eeceab017260370cf540e1d25442c59665fd07d1b09b66d63bb0c282887'

    docker pull "$image" >/dev/null
    docker image inspect --format '{{range .RepoDigests}}{{println .}}{{end}}' "$image" > "$output/repo-digests.txt"
    grep -Fx "$image" "$output/repo-digests.txt"
    docker save "$image" -o "$output/image.tar"
    docker run --rm --network none -e SYFT_CHECK_FOR_APP_UPDATE=false \
        -v "$output:/evidence:ro" "$syft" scan docker-archive:/evidence/image.tar -o cyclonedx-json \
        > "$output/sbom.cdx.json"
    rm "$output/image.tar"
    if [[ "$mode" == --scan ]]; then
        docker run --rm -e GRYPE_CHECK_FOR_APP_UPDATE=false \
            -e GRYPE_DB_UPDATE_AVAILABLE_TIMEOUT=20s -e GRYPE_DB_UPDATE_DOWNLOAD_TIMEOUT=120s \
            -v "$output:/evidence:ro" "$grype" "sbom:/evidence/sbom.cdx.json" -o json \
            > "$output/scan.json"
    fi
fi
python3 - "$output" "$mode" <<'PY'
import json
from collections import Counter
from pathlib import Path
import sys

folder = Path(sys.argv[1])
inventory = json.loads((folder / "sbom.cdx.json").read_text())
components = inventory["components"]
assert inventory["bomFormat"] == "CycloneDX" and components
print(f"Inventory components: {len(components)}")
if sys.argv[2] != "--inventory-only":
    report = json.loads((folder / "scan.json").read_text())
    counts = Counter(match["vulnerability"]["severity"] for match in report["matches"])
    print(f"Matches by severity: {dict(sorted(counts.items()))}")
    print("Review the scanner and vulnerability database metadata in scan.json.")
PY
