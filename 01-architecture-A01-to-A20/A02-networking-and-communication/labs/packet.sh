#!/bin/sh
set -eu

dig +notcp +tries=1 +time=1 api A
expected_status=$(dig +notcp +tries=1 +time=1 +noall +comments     wrong-name.invalid A)
printf '%s\n' "$expected_status"
test -z "$(dig +notcp +tries=1 +time=1 +short wrong-name.invalid A)"
curl -fsS --retry 8 --retry-connrefused --retry-delay 1 --max-time 3 http://api:8000/health
echo
capture=$(mktemp)
trap 'rm -f "$capture"' EXIT
timeout 6 tcpdump -i any -nn -l -c 4 'tcp port 8000' >"$capture" 2>&1 &
capture_pid=$!
for _ in 1 2 3 4 5 6 7 8 9 10; do
    grep -q 'listening on' "$capture" && break
    sleep 0.1
done
curl -fsSv --max-time 3 http://api:8000/health
echo
ss -tan 'dport = :8000'
wait "$capture_pid"
cat "$capture"
grep -F 'Flags [S]' "$capture"
grep -F 'Flags [S.]' "$capture"
