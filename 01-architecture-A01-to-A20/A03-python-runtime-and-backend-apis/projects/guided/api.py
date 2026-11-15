"""Local CRUD project with explicit tenant and role checks."""

from collections.abc import Mapping
from dataclasses import dataclass
import hmac
from threading import Lock
from typing import Annotated
from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, ConfigDict, Field


@dataclass(frozen=True)
class Principal:
    tenant: str
    can_write: bool


class Draft(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    title: str = Field(min_length=1, max_length=100)


class Item(Draft):
    id: str


def create_app(credentials: Mapping[str, Principal]) -> FastAPI:
    app = FastAPI(title="Local inventory")
    auth = HTTPBearer(auto_error=False)
    store: dict[tuple[str, str], Item] = {}
    mutex = Lock()
    tokens = tuple((token.encode(), principal) for token, principal in credentials.items())

    def identity(
        credential: Annotated[HTTPAuthorizationCredentials | None, Depends(auth)],
    ) -> Principal:
        if credential is not None:
            supplied = credential.credentials.encode()
            for token, principal in tokens:
                if hmac.compare_digest(token, supplied):
                    return principal
        raise HTTPException(
            401, "Valid fixture credential required", headers={"WWW-Authenticate": "Bearer"}
        )

    def require_write(principal: Principal) -> None:
        if not principal.can_write:
            raise HTTPException(403, "Write permission required")

    def lookup(key: tuple[str, str]) -> Item:
        item = store.get(key)
        if item is None:
            raise HTTPException(404, "Item not found")
        return item

    @app.post("/items", status_code=201, response_model=Item)
    def insert(body: Draft, response: Response, principal: Principal = Depends(identity)) -> Item:
        require_write(principal)
        item = Item(id=uuid4().hex, title=body.title)
        with mutex:
            store[principal.tenant, item.id] = item
        response.headers["Location"] = f"/items/{item.id}"
        return item

    @app.get("/items/{item_id}", response_model=Item)
    def read(item_id: str, principal: Principal = Depends(identity)) -> Item:
        with mutex:
            return lookup((principal.tenant, item_id))

    @app.put("/items/{item_id}", response_model=Item)
    def replace(item_id: str, body: Draft, principal: Principal = Depends(identity)) -> Item:
        require_write(principal)
        key = (principal.tenant, item_id)
        with mutex:
            lookup(key)
            store[key] = Item(id=item_id, title=body.title)
            return store[key]

    @app.delete("/items/{item_id}", status_code=204)
    def remove(item_id: str, principal: Principal = Depends(identity)) -> Response:
        require_write(principal)
        key = (principal.tenant, item_id)
        with mutex:
            lookup(key)
            del store[key]
        return Response(status_code=204)

    return app


app = create_app(
    {
        "fixture-a-write": Principal("a", True),
        "fixture-a-read": Principal("a", False),
        "fixture-b-write": Principal("b", True),
    }
)
