from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseStoreRepo(ABC):
    """Persistence interface for the document store.

    We keep this small and CRUD-focused so the FastAPI routes stay the same
    regardless of whether the backend is MongoDB or TinyDB.
    """

    @abstractmethod
    def create(self, doc: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def list(self, *, limit: int = 50) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def get(self, doc_id: str) -> dict[str, Any] | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, doc_id: str, patch: dict[str, Any]) -> dict[str, Any] | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, doc_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def search(self, *, q: str | None = None, tag: str | None = None, source: str | None = None, limit: int = 50) -> list[dict[str, Any]]:
        raise NotImplementedError
