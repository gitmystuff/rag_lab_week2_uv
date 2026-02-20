from __future__ import annotations

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    """Relational (Postgres) document metadata."""

    title: str
    source: str | None = None


class StoreDocumentCreate(BaseModel):
    """Document-store record (MongoDB/TinyDB).

    This is intentionally RAG-friendly: it includes optional content and tags.
    """

    title: str
    source: str | None = None
    content: str | None = None
    tags: list[str] = Field(default_factory=list)


class StoreDocumentUpdate(BaseModel):
    title: str | None = None
    source: str | None = None
    content: str | None = None
    tags: list[str] | None = None
