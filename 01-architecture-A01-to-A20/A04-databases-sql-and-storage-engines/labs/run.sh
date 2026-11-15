#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
case "${1:-}" in L1|L2|L3|L4|guided|ledger) ;; *) echo "Usage: bash run.sh L1|L2|L3|L4|guided|ledger" >&2; exit 2;; esac
scenario=$1
scratch=$(mktemp -d)
cid=
secret=$(python3 -c 'import secrets; print(secrets.token_hex(24))')
cleanup() {
    local status=$?
    if [[ -n "$cid" ]]; then
        if (( status )); then docker logs --tail 40 "$cid" >&2 || true; fi
        docker rm -fv "$cid" >/dev/null || true
    fi
    rm -rf "$scratch"
}
trap cleanup EXIT
cid=$(docker run -d --network none --memory 512m --pids-limit 100 \
    -e "POSTGRES_PASSWORD=$secret" -e POSTGRES_DB=practice \
    postgres:18 -c deadlock_timeout=200ms)
ready() {
    for _ in $(seq 1 60); do
        if docker exec "$cid" pg_isready -h 127.0.0.1 -U postgres -d practice >/dev/null 2>&1; then
            return
        fi
        sleep .25
    done
    echo "PostgreSQL did not become ready" >&2
    return 1
}
# Authenticate inside the private container without copying credentials into source or logs.
pg() {
    docker exec -i "$cid" sh -c 'PGPASSWORD=$POSTGRES_PASSWORD exec psql -h 127.0.0.1 -X -U postgres -d practice -v ON_ERROR_STOP=1 "$@"' psql "$@"
}
expect() {
    local observed
    observed=$(pg -Atc "$1")
    printf '%s → %s\n' "$1" "$observed"
    test "$observed" = "$2"
}
active_sleep() {
    for _ in $(seq 1 60); do
        if [[ $(pg -Atc "SELECT count(*) FROM pg_stat_activity WHERE application_name='$1' AND wait_event='PgSleep'") == 1 ]]; then
            return
        fi
        sleep .08
    done
    echo "Session $1 did not enter its barrier" >&2
    return 1
}
query_plan() {
    pg < plans.sql | tee "$scratch/plan"
    grep -Eq 'Seq Scan' "$scratch/plan"
    grep -Eq 'Index (Only )?Scan|Bitmap Index Scan' "$scratch/plan"
    expect 'SELECT count(*) FROM plan_items WHERE rare' 1
}
crash_recover() {
    pg -c "CREATE TABLE crash_markers (label text PRIMARY KEY); INSERT INTO crash_markers VALUES ('committed');"
    pg >"$scratch/writer" 2>&1 <<'SQL' &
SET application_name='lab-crash-writer';
BEGIN;
INSERT INTO crash_markers VALUES ('incomplete');
SELECT pg_sleep(30);
COMMIT;
SQL
    local writer=$!
    active_sleep lab-crash-writer
    docker kill --signal KILL "$cid" >/dev/null
    wait "$writer" || true
    docker start "$cid" >/dev/null
    ready
    expect "SELECT string_agg(label, ',' ORDER BY label) FROM crash_markers" committed
}
ready
case "$scenario" in
    L1) query_plan ;;
    L2)
        pg -c 'CREATE TABLE inventory(id int PRIMARY KEY, quantity int NOT NULL); INSERT INTO inventory VALUES (1,5),(2,5);'
        pg >"$scratch/stale" 2>&1 <<'SQL' &
SET application_name='lab-stale';
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT quantity AS old_quantity FROM inventory WHERE id=1 \gset
SELECT pg_sleep(3);
UPDATE inventory SET quantity=(:old_quantity - 1) WHERE id=1;
COMMIT;
SQL
        stale=$!
        active_sleep lab-stale
        pg -c 'UPDATE inventory SET quantity=quantity-1 WHERE id=1;'
        wait "$stale"
        expect 'SELECT quantity FROM inventory WHERE id=1' 4
        pg -c 'UPDATE inventory SET quantity=quantity-1 WHERE id=1;'
        expect 'SELECT quantity FROM inventory WHERE id=1' 3
        pg >"$scratch/first" 2>&1 <<'SQL' &
\set VERBOSITY verbose
SET application_name='lab-deadlock-first';
BEGIN;
UPDATE inventory SET quantity=quantity WHERE id=1;
SELECT pg_sleep(3);
UPDATE inventory SET quantity=quantity WHERE id=2;
COMMIT;
SQL
        first=$!
        active_sleep lab-deadlock-first
        pg >"$scratch/second" 2>&1 <<'SQL' &
\set VERBOSITY verbose
BEGIN;
UPDATE inventory SET quantity=quantity WHERE id=2;
UPDATE inventory SET quantity=quantity WHERE id=1;
COMMIT;
SQL
        second=$!
        successes=0
        if wait "$first"; then successes=$((successes+1)); fi
        if wait "$second"; then successes=$((successes+1)); fi
        test "$successes" = 1
        grep -F '40P01' "$scratch/first" "$scratch/second"
        pg -c 'BEGIN; UPDATE inventory SET quantity=quantity WHERE id=1; UPDATE inventory SET quantity=quantity WHERE id=2; COMMIT;'
        ;;
    L3) crash_recover ;;
    L4)
        pg -c "CREATE TABLE profiles (id int PRIMARY KEY, display_name text NOT NULL); INSERT INTO profiles VALUES (1,'Ada');"
        pg >"$scratch/reader" 2>&1 <<'SQL' &
SET application_name='lab-reader';
BEGIN;
SELECT display_name FROM profiles;
SELECT pg_sleep(4);
COMMIT;
SQL
        reader=$!
        active_sleep lab-reader
        if pg -c "SET lock_timeout='250ms'; ALTER TABLE profiles RENAME COLUMN display_name TO label;" >"$scratch/migration" 2>&1; then
            echo "expected access-exclusive lock to conflict with the reader" >&2
            exit 1
        fi
        grep -F 'lock timeout' "$scratch/migration"
        wait "$reader"
        pg -c 'BEGIN; ALTER TABLE profiles RENAME COLUMN display_name TO label; ROLLBACK;'
        expect 'SELECT display_name FROM profiles WHERE id=1' Ada
        pg -c 'ALTER TABLE profiles ADD COLUMN label text; UPDATE profiles SET label=display_name WHERE label IS NULL;'
        expect 'SELECT display_name FROM profiles WHERE id=1' Ada
        expect 'SELECT coalesce(label,display_name) FROM profiles WHERE id=1' Ada
        ;;
    guided)
        query_plan
        pg < ../projects/guided/sandbox.sql
        expect 'SELECT count(*) FROM transfer_totals WHERE balance = 60' 1
        crash_recover
        ;;
    ledger)
        pg < ../projects/independent/001_ledger.sql
        pg -c "SELECT submit_order('old','before-migration',600);"
        pg < ../projects/independent/002_origin.sql
        pg < ../projects/independent/002_origin.sql
        pg < ../projects/independent/check.sql
        pg -Atc "SELECT submit_order('race','repeat', 444)" > "$scratch/race1" &
        left=$!
        pg -Atc "SELECT submit_order('race','repeat', 444)" > "$scratch/race2" &
        right=$!
        wait "$left"
        wait "$right"
        cmp "$scratch/race1" "$scratch/race2"
        expect "SELECT count(*) FROM order_entries WHERE tenant='race'" 1
        crash_recover
        expect "SELECT submit_order('race','repeat',444)" "$(cat "$scratch/race1")"
        expect "SELECT count(*) FROM order_entries WHERE tenant='race'" 1
        ;;
esac
printf '%s verified\n' "$scenario"
