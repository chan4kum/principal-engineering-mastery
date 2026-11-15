"""Isolated recovery and game-day scenarios with machine-readable evidence."""

import argparse
import json
import socket
import sqlite3
import struct
import time
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory


def copy_database(source: Path, target: Path) -> None:
    with (
        closing(sqlite3.connect(source)) as original,
        closing(sqlite3.connect(target)) as restored,
    ):
        original.backup(restored)


def verify(path: Path) -> int:
    with closing(sqlite3.connect(path)) as db:
        integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise ValueError(integrity)
        return db.execute("SELECT sum(cents) FROM orders").fetchone()[0]


def recovery(directory: Path, broken: bool = False) -> dict:
    source, backup, target = (
        directory / name for name in ("source.sqlite", "backup.sqlite", "target.sqlite")
    )
    if any(path.exists() for path in (source, backup, target)):
        raise ValueError("use an empty drill directory")
    with closing(sqlite3.connect(source)) as db, db:
        db.execute("CREATE TABLE orders(cents INTEGER NOT NULL CHECK(cents>0))")
        db.execute("INSERT INTO orders VALUES (125),(375)")
    copy_database(source, backup)
    # Roll back an invalid migration without altering the committed invariant.
    with closing(sqlite3.connect(source)) as db:
        db.execute("BEGIN")
        db.execute("ALTER TABLE orders ADD COLUMN note TEXT")
        db.execute("UPDATE orders SET cents=999")
        db.rollback()
        assert (
            db.execute("SELECT count(*) FROM pragma_table_info('orders')").fetchone()[0]
            == 1
        )
    target_corrupt = False
    if broken:
        target.write_bytes(b"disposable damaged restore target" * 100)
        try:
            verify(target)
        except sqlite3.DatabaseError:
            target_corrupt = True
            target.unlink()
    started = time.monotonic()
    copy_database(backup, target)
    restored = verify(target)
    return {
        "baseline_cents": verify(source),
        "restored_cents": restored,
        "target_corrupt": target_corrupt,
        "restore_and_verify_ms": (time.monotonic() - started) * 1000,
    }


def cpu_probe(broken: bool) -> dict[str, float]:
    start, cpu_start = time.monotonic(), time.process_time()
    if broken:
        while time.process_time() - cpu_start < 0.02:
            pass
    else:
        time.sleep(0.025)
    elapsed = time.monotonic() - start
    return {
        "wall_ms": elapsed * 1000,
        "cpu_ms": (time.process_time() - cpu_start) * 1000,
    }


def lock_probe(path: Path, broken: bool) -> dict[str, bool]:
    with (
        closing(sqlite3.connect(path)) as owner,
        closing(sqlite3.connect(path, timeout=0.025)) as waiter,
    ):
        owner.execute("CREATE TABLE IF NOT EXISTS fixture (id INT)")
        if broken:
            owner.execute("BEGIN IMMEDIATE")
        try:
            with waiter:
                waiter.execute("INSERT INTO fixture VALUES (1)")
        except sqlite3.OperationalError as error:
            if getattr(error, "sqlite_errorcode", None) != sqlite3.SQLITE_BUSY:
                raise
            return {"database_busy": True}
        finally:
            owner.rollback()
        return {"database_busy": False}


def dns_probe(broken: bool) -> dict[str, int]:
    """One fixed DNS query and synthetic fixture peer on UDP loopback."""
    query = (
        struct.pack("!6H", 9, 0x0100, 1, 0, 0, 0)
        + b"\x07fixture\x04test\x00\x00\x01\x00\x01"
    )
    with (
        socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as resolver,
        socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client,
    ):
        resolver.bind(("127.0.0.1", 0))
        resolver.settimeout(1)
        client.settimeout(1)
        client.sendto(query, resolver.getsockname())
        incoming, sender = resolver.recvfrom(128)
        assert incoming == query
        flags = 0x8183 if broken else 0x8180
        reply = struct.pack("!6H", 9, flags, 1, 0 if broken else 1, 0, 0) + query[12:]
        if not broken:
            reply += (
                b"\xc0\x0c"
                + struct.pack("!HHIH", 1, 1, 60, 4)
                + socket.inet_aton("127.0.0.1")
            )
        resolver.sendto(reply, sender)
        received, peer = client.recvfrom(128)
        identifier, header = struct.unpack_from("!HH", received)
        assert identifier == 9 and peer == resolver.getsockname()
        return {"dns_rcode": header & 15}


def observe(directory: Path, fault: str) -> dict:
    if fault not in {"none", "cpu", "lock", "dns"}:
        raise ValueError("unknown fault")
    return {
        **cpu_probe(fault == "cpu"),
        **lock_probe(directory / "lock.sqlite", fault == "lock"),
        **dns_probe(fault == "dns"),
    }


def classify(evidence: dict) -> str:
    if evidence["database_busy"]:
        return "lock"
    if evidence["dns_rcode"] != 0:
        return "dns"
    if evidence["cpu_ms"] >= 15:
        return "cpu"
    return "none"


def game_day(directory: Path, fault: str) -> dict:
    timeline = {
        "baseline": observe(directory, "none"),
        "incident": observe(directory, fault),
        "recovery": observe(directory, "none"),
    }
    return {
        "timeline": timeline,
        "diagnosis": classify(timeline["incident"]),
        "recovered": classify(timeline["recovery"]) == "none",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", choices=["cpu", "lock", "dns", "restore", "corrupt"])
    args = parser.parse_args()
    with TemporaryDirectory() as directory:
        path = Path(directory)
        if args.fixture in {"restore", "corrupt"}:
            result = recovery(path, args.fixture == "corrupt")
        else:
            result = game_day(path, args.fixture)
        print(json.dumps(result, indent=2))
