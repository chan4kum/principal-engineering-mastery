"""A local approval gate for exactly one simulated side effect."""

import hashlib
import json
import sqlite3
from contextlib import closing, contextmanager
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4


@dataclass(frozen=True)
class Principal:
    """Trusted application identity in the fixture, not model-supplied data."""

    actor: str
    tenant: str
    role: str


class Denied(Exception):
    pass


def digest(tenant: str, action: str, message: str) -> str:
    encoded = json.dumps([tenant, action, message], separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


class Coordinator:
    def __init__(self, path: Path) -> None:
        self.path = path
        with closing(sqlite3.connect(path)) as db:
            db.executescript("""
              CREATE TABLE IF NOT EXISTS proposals(
                id TEXT PRIMARY KEY, tenant TEXT NOT NULL, author TEXT NOT NULL,
                action TEXT NOT NULL, payload TEXT NOT NULL, digest TEXT NOT NULL,
                reviewer TEXT, approved_until INTEGER
              );
              CREATE TABLE IF NOT EXISTS effects(
                proposal TEXT PRIMARY KEY, tenant TEXT NOT NULL, notice TEXT NOT NULL
              );
              CREATE TABLE IF NOT EXISTS audit(
                seq INTEGER PRIMARY KEY, proposal TEXT NOT NULL, actor TEXT NOT NULL, event TEXT NOT NULL
              );
            """)

    @contextmanager
    def transaction(self):
        with closing(sqlite3.connect(self.path, timeout=3)) as db, db:
            db.execute("BEGIN IMMEDIATE")
            yield db

    @staticmethod
    def find(db, proposal: str, tenant: str):
        found = db.execute(
            "SELECT author,action,digest,reviewer,approved_until FROM proposals WHERE id=? AND tenant=?",
            (proposal, tenant),
        ).fetchone()
        if found is None:
            raise Denied("proposal outside authority")
        return found

    def propose(self, actor: Principal, action: str, message: str) -> tuple[str, str]:
        if (
            actor.role != "operator"
            or action != "notice"
            or not message.strip()
            or len(message) > 300
        ):
            raise Denied("proposal outside policy")
        key, identity = uuid4().hex, digest(actor.tenant, action, message)
        with self.transaction() as db:
            db.execute(
                "INSERT INTO proposals VALUES (?,?,?,?,?,?,NULL,NULL)",
                (
                    key,
                    actor.tenant,
                    actor.actor,
                    action,
                    message,
                    identity,
                ),
            )
            db.execute(
                "INSERT INTO audit(proposal,actor,event) VALUES (?,?,?)",
                (key, actor.actor, "proposed"),
            )
        return key, identity

    def approve(
        self, actor: Principal, proposal: str, exact: str, now: int, ttl: int
    ) -> None:
        with self.transaction() as db:
            author, _, identity, _, _ = self.find(db, proposal, actor.tenant)
            if (
                actor.role != "reviewer"
                or actor.actor == author
                or exact != identity
                or not 1 <= ttl <= 60
            ):
                raise Denied("approval outside policy")
            db.execute(
                "UPDATE proposals SET reviewer=?,approved_until=? WHERE id=?",
                (actor.actor, now + ttl, proposal),
            )
            db.execute(
                "INSERT INTO audit(proposal,actor,event) VALUES (?,?,?)",
                (proposal, actor.actor, "approved"),
            )

    def execute(self, actor: Principal, proposal: str, message: str, now: int) -> bool:
        with self.transaction() as db:
            author, action, identity, reviewer, until = self.find(
                db, proposal, actor.tenant
            )
            if actor.role != "operator" or actor.actor != author or action != "notice":
                raise Denied("execution outside authority")
            if (
                reviewer is None
                or now >= until
                or digest(actor.tenant, action, message) != identity
            ):
                raise Denied("current exact approval required")
            inserted = db.execute(
                "INSERT OR IGNORE INTO effects VALUES (?,?,?)",
                (proposal, actor.tenant, message),
            ).rowcount
            db.execute(
                "INSERT INTO audit(proposal,actor,event) VALUES (?,?,?)",
                (
                    proposal,
                    actor.actor,
                    "executed" if inserted else "replayed",
                ),
            )
            return bool(inserted)

    def history(self, actor: Principal, proposal: str) -> list[str]:
        with closing(sqlite3.connect(self.path)) as db:
            self.find(db, proposal, actor.tenant)
            return [
                event
                for (event,) in db.execute(
                    "SELECT event FROM audit WHERE proposal=? ORDER BY seq", (proposal,)
                )
            ]

    def effects(self, tenant: str) -> int:
        with closing(sqlite3.connect(self.path)) as db:
            return db.execute(
                "SELECT count(*) FROM effects WHERE tenant=?", (tenant,)
            ).fetchone()[0]
