from __future__ import annotations

from app.config import STORE_BACKEND
from app.store.base import BaseStoreRepo
from app.store.mongo_repo import MongoStoreRepo
from app.store.tiny_repo import TinyStoreRepo


def get_store_repo() -> BaseStoreRepo:
    """Factory that selects the store backend.

    - STORE_BACKEND=mongo  -> MongoDB (local)
    - STORE_BACKEND=tinydb -> TinyDB JSON file fallback
    """

    if STORE_BACKEND == "mongo":
        return MongoStoreRepo()
    return TinyStoreRepo()
