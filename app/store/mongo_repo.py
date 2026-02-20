from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pymongo import MongoClient

from app.config import MONGO_COLLECTION, MONGO_DB, MONGO_URL
from app.store.base import BaseStoreRepo


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class MongoStoreRepo(BaseStoreRepo):
    def __init__(self) -> None:
        self._client = MongoClient(MONGO_URL)
        self._db = self._client[MONGO_DB]
        self._col = self._db[MONGO_COLLECTION]

        # Helpful indexes for class demos (safe to call repeatedly)
        try:
            self._col.create_index("id", unique=True)
            self._col.create_index("source")
            self._col.create_index("tags")
        except Exception:
            # Index creation can fail in restricted environments; not fatal for the lab.
            pass

    def create(self, doc: dict[str, Any]) -> dict[str, Any]:
        out = dict(doc)
        out["id"] = out.get("id") or str(uuid4())
        out["created_at"] = out.get("created_at") or _now_iso()
        out.setdefault("tags", [])
        self._col.insert_one(out)
        return self._strip(out)

    def list(self, *, limit: int = 50) -> list[dict[str, Any]]:
        cursor = self._col.find({}, {"_id": 0}).sort("created_at", -1).limit(int(limit))
        return [self._strip(d) for d in cursor]

    def get(self, doc_id: str) -> dict[str, Any] | None:
        d = self._col.find_one({"id": doc_id}, {"_id": 0})
        return self._strip(d) if d else None

    def update(self, doc_id: str, patch: dict[str, Any]) -> dict[str, Any] | None:
        patch = {k: v for k, v in patch.items() if v is not None}
        if not patch:
            return self.get(doc_id)

        self._col.update_one({"id": doc_id}, {"$set": patch})
        return self.get(doc_id)

    def delete(self, doc_id: str) -> bool:
        res = self._col.delete_one({"id": doc_id})
        return bool(res.deleted_count)

    def search(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        source: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        query: dict[str, Any] = {}
        if tag:
            query["tags"] = tag
        if source:
            query["source"] = source
        if q:
            # Simple contains search over title/content for class purposes.
            query["$or"] = [
                {"title": {"$regex": q, "$options": "i"}},
                {"content": {"$regex": q, "$options": "i"}},
            ]

        cursor = self._col.find(query, {"_id": 0}).sort("created_at", -1).limit(int(limit))
        return [self._strip(d) for d in cursor]

    @staticmethod
    def _strip(d: dict[str, Any] | None) -> dict[str, Any]:
        if not d:
            return {}
        d = dict(d)
        d.pop("_id", None)
        return d
