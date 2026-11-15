#!/usr/bin/env bash
set -euo pipefail
cid=$(docker run -d --network none --memory 128m --pids-limit 32 redis:8-alpine --save "" --appendonly no)
trap 'docker rm -fv "$cid" >/dev/null' EXIT
redis() { docker exec "$cid" redis-cli --raw "$@"; }
for _ in $(seq 1 30); do
    if [[ $(redis PING 2>/dev/null || true) == PONG ]]; then break; fi
    sleep .15
done
test "$(redis SET lab:key first EX 60)" = OK
test "$(redis GET lab:key)" = first
ttl=$(redis TTL lab:key)
test "$ttl" -gt 0
test "$(redis PEXPIRE lab:key 0)" = 1
test "$(redis EXISTS lab:key)" = 0
test "$(redis SET lab:key repair EX 60)" = OK
test "$(redis GET lab:key)" = repair
printf 'Redis hit, forced expiry, miss and refill verified\n'
