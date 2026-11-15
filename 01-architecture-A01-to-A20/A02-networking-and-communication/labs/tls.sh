#!/bin/sh
set -eu

tmp=$(mktemp -d)
server=
cleanup() {
    if [ -n "$server" ]; then
        kill "$server" 2>/dev/null || true
        wait "$server" 2>/dev/null || true
    fi
    rm -rf "$tmp"
}
trap cleanup EXIT INT TERM
cd "$tmp"
openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 1     -subj /CN=A02-test-root -addext 'basicConstraints=critical,CA:TRUE'     -addext 'keyUsage=critical,keyCertSign,cRLSign' -keyout root.key -out root.crt 2>/dev/null
openssl req -newkey rsa:2048 -nodes -subj /CN=service.test     -keyout leaf.key -out leaf.csr 2>/dev/null
printf 'subjectAltName=DNS:service.test\nextendedKeyUsage=serverAuth\n' > extensions
openssl x509 -req -in leaf.csr -CA root.crt -CAkey root.key -CAcreateserial     -extfile extensions -days 1 -out leaf.crt 2>/dev/null
openssl s_server -accept 127.0.0.1:8443 -cert leaf.crt -key leaf.key -www -quiet >server.log 2>&1 &
server=$!
for _ in 1 2 3 4 5 6 7 8 9 10; do
    ss -H -ltn 'sport = :8443' | grep -q . && break
    sleep 0.1
done
inspect() {
    timeout 5 openssl s_client -connect 127.0.0.1:8443 -servername service.test \
        -verify_return_error -showcerts "$@" </dev/null
}
if inspect -verify_hostname service.test >untrusted.log 2>&1; then
    echo 'unexpected success without the lab CA' >&2
    exit 1
fi
grep -E 'verify error|Verification error' untrusted.log
if inspect -CAfile root.crt -verify_hostname wrong.test >wrong-name.log 2>&1; then
    echo 'unexpected success with wrong identity' >&2
    exit 1
fi
grep -F 'hostname mismatch' wrong-name.log
inspect -CAfile root.crt -verify_hostname service.test >trusted.log 2>&1
grep -E 'subject=|issuer=|Verify return code: 0' trusted.log
grep -F 'Verify return code: 0' trusted.log
