"""A scoped, revision-aware extractive RAG application."""

import importlib.util
from functools import lru_cache
from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

spec = importlib.util.spec_from_file_location(
    "a12_rank", Path(__file__).resolve().parents[1] / "guided/benchmark.py"
)
assert spec is not None and spec.loader is not None
rank = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rank)


class Search:
    def __init__(self) -> None:
        self.current: dict[tuple[str, str], tuple[int, str | None]] = {}
        self.query_cache = lru_cache(maxsize=256)(self._search)

    def replace(
        self, tenant: str, document: str, revision: int, text: str | None
    ) -> bool:
        if not tenant or not document or revision < 1:
            raise ValueError("invalid source identity")
        key = (tenant, document)
        if revision <= self.current.get(key, (0, None))[0]:
            return False
        self.current[key] = (revision, text)
        self.query_cache.cache_clear()
        return True

    def _search(
        self, tenant: str, question: str, k: int
    ) -> tuple[tuple[str, int, str], ...]:
        allowed = {
            doc: text
            for (owner, doc), (_, text) in self.current.items()
            if owner == tenant and text is not None
        }
        ranked = rank.fuse(
            rank.lexical(question, allowed), rank.dense(question, allowed)
        )
        return tuple(
            (doc, self.current[(tenant, doc)][0], allowed[doc]) for doc in ranked[:k]
        )

    def answer(self, tenant: str, question: str, k: int = 3):
        if not 1 <= k <= 10 or not question.strip() or len(question) > 500:
            raise ValueError("query outside fixture bounds")
        evidence = self.query_cache(tenant, question, k)
        return {
            "abstained": not evidence,
            "evidence": [
                {"source": doc, "revision": revision, "quote": quote}
                for doc, revision, quote in evidence
            ],
        }


class Question(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    k: int = Field(3, strict=True, ge=1, le=10)


def create_app(index: Search, fixture_identities: dict[str, str]) -> FastAPI:
    app = FastAPI()
    auth = HTTPBearer(auto_error=False)
    identities = dict(fixture_identities)

    @app.post("/answer")
    async def answer(
        body: Question,
        token: Annotated[HTTPAuthorizationCredentials | None, Depends(auth)],
    ):
        tenant = identities.get(token.credentials) if token is not None else None
        if tenant is None:
            raise HTTPException(
                401,
                "fixture credential required",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            return index.answer(tenant, body.text, body.k)
        except ValueError as error:
            raise HTTPException(422, str(error)) from error

    return app
