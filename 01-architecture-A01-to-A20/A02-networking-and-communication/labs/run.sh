#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
project="${A02_LAB_PROJECT:-pem-a02-$$}"
compose=(docker compose -p "$project" -f compose.yaml)
cleanup() {
    local status=$?
    if (( status != 0 )); then
        "${compose[@]}" logs --tail 40 || true
    fi
    "${compose[@]}" down --remove-orphans
}
trap cleanup EXIT
if (( $# != 1 )); then
    echo "Usage: bash run.sh L1|L2|L3|L4" >&2
    exit 2
fi
"${compose[@]}" build api packet-client
exec_service() {
    "${compose[@]}" exec -T "$@"
}

case "$1" in
    L1)
        "${compose[@]}" up -d api packet-client
        exec_service packet-client sh /lab/packet.sh
        ;;
    L2)
        "${compose[@]}" up -d packet-client
        exec_service packet-client sh /lab/tls.sh
        ;;
    L3)
        "${compose[@]}" up -d routed-api gateway routed-client
        exec_service routed-client ip route replace 172.31.242.0/24 via 172.31.241.2
        exec_service routed-client ip route get 172.31.242.10
        rule=(-s 172.31.241.10/32 -d 172.31.242.10/32 -p tcp --dport 8000 -j SNAT --to-source 172.31.242.2)
        exec_service gateway iptables -t nat -A POSTROUTING "${rule[@]}"
        url=http://172.31.242.10:8000/peer
        probe() {
            exec_service routed-client curl -fsS --retry "${1:-0}" --retry-connrefused \
                --retry-delay 1 --max-time 2 "$url"
        }
        probe 6 | grep -F '172.31.242.2'
        exec_service gateway iptables -t nat -D POSTROUTING "${rule[@]}"
        if probe; then
            echo "expected a missing return path without SNAT" >&2
            exit 1
        fi
        exec_service gateway iptables -t nat -A POSTROUTING "${rule[@]}"
        probe | grep -F '172.31.242.2'
        ;;
    L4)
        "${compose[@]}" up -d routed-api proxy proxy-client
        base=http://proxy:8080
        request() {
            exec_service proxy-client curl -fNsS --max-time 5 "$@"
        }
        request --retry 8 --retry-connrefused --retry-delay 1 "$base/health" | grep -F '"ready":true'
        good=$(request "$base/stream")
        printf '%s\n' "$good"
        grep -Fxq 'last' <<<"$good"
        if partial=$(request "$base/broken"); then
            echo "expected an interrupted stream" >&2
            exit 1
        fi
        printf '%s\n' "$partial"
        grep -Fxq 'first' <<<"$partial"
        if grep -Fxq 'last' <<<"$partial"; then
            echo "unexpected last chunk after timeout" >&2
            exit 1
        fi
        request "$base/stream" | grep -Fx 'last'
        ;;
    *)
        echo "Choose L1, L2, L3, or L4" >&2
        exit 2
        ;;
esac
