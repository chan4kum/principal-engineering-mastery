#!/bin/sh
set -eu
events=/sys/fs/cgroup/memory.events
oom_kills() { awk '$1 == "oom_kill" {print $2}' "$events"; }
before=$(oom_kills)
status=0
python /lab/memory_pressure.py --break || status=$?
after=$(oom_kills)
printf 'Worker exit status: %s, cgroup oom_kill: %s → %s\n' "$status" "$before" "$after"
test "$status" = 137
test "$after" -gt "$before"
