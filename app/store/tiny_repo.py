from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from tinydb import Query, TinyDB

from app.config import TINYDB_FILE
from app.store.base import BaseStoreRepo


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class TinyStoreRepo(BaseStoreRepo):
    def __init__(self) -> None:
        self._db = TinyDB(TINYDB_FILE)

    def create(self, doc: dict[str, Any]) -> dict[str, Any]:
        out = dict(doc)
        out["id"] = out.get("id") or str(uuid4())
        out["created_at"] = out.get("created_at") or _now_iso()
        out.setdefault("tags", [])
        self._db.insert(out)
        return out

    def list(self, *, limit: int = 50) -> list[dict[str, Any]]:
        docs = sorted(self._db.all(), key=lambda d: d.get("created_at", ""), reverse=True)
        return docs[: int(limit)]

    def get(self, doc_id: str) -> dict[str, Any] | None:
        return self._db.get(Query().id == doc_id)

    def update(self, doc_id: str, patch: dict[str, Any]) -> dict[str, Any] | None:
        patch = {k: v for k, v in patch.items() if v is not None}
        if not patch:
            return self.get(doc_id)
        self._db.update(patch, Query().id == doc_id)
        return self.get(doc_id)

    def delete(self, doc_id: str) -> bool:
        before = len(self._db)
        self._db.remove(Query().id == doc_id)
        after = len(self._db)
        return after < before

    def search(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        source: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        docs = self._db.all()

        def match(d: dict[str, Any]) -> bool:
            if tag and tag not in (d.get("tags") or []):
                return False
            if source and d.get("source") != source:
                return False
            if q:
                ql = q.lower()
                text = f"{d.get('title','')} {d.get('content','')}".lower()
                return ql in text
            return True

        out = [d for d in docs if match(d)]
        out = sorted(out, key=lambda d: d.get("created_at", ""), reverse=True)
        return out[: int(limit)]
