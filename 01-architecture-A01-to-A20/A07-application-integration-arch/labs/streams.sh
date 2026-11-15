#!/usr/bin/env bash
set -euo pipefail
cid=$(docker run -d --network none --memory 128m --pids-limit 32 redis:8-alpine --save "" --appendonly no)
trap 'docker rm -fv "$cid" >/dev/null' EXIT
redis() { docker exec "$cid" redis-cli --raw "$@"; }
for _ in $(seq 1 30); do
    if [[ $(redis PING 2>/dev/null || true) == PONG ]]; then break; fi
    sleep .15
done
test "$(redis XGROUP CREATE orders workers 0 MKSTREAM)" = OK
id=$(redis XADD orders '*' event_id fixture-1)
redis XREADGROUP GROUP workers worker-a COUNT 1 STREAMS orders '>' | grep -Fx "$id"
test "$(redis XPENDING orders workers | head -1)" = 1
redis XAUTOCLAIM orders workers worker-b 0 0-0 COUNT 1 | grep -Fx "$id"
test "$(redis XACK orders workers "$id")" = 1
test "$(redis XPENDING orders workers | head -1)" = 0
test "$(redis XLEN orders)" = 1
printf 'Redis Streams redelivery and acknowledgement verified\n'
