from __future__ import annotations

from fastapi import FastAPI, HTTPException

from app.db import get_conn
from app.models import DocumentCreate, StoreDocumentCreate, StoreDocumentUpdate
from app.store import get_store_repo

app = FastAPI(title="RAG Data API")

# Postgres (existing module)
# -----------------------------------------------------------------------------


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/documents")
def create_document(doc: DocumentCreate):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO documents (title, source)
                VALUES (%s, %s)
                RETURNING id, title, source, created_at
                """,
                (doc.title, doc.source),
            )
            return cur.fetchone()


@app.get("/documents")
def list_documents():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM documents ORDER BY created_at DESC")
            return cur.fetchall()


@app.get("/documents/{doc_id}")
def get_document(doc_id: str):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM documents WHERE id = %s", (doc_id,))
            row = cur.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="Document not found")
            return row


@app.delete("/documents/{doc_id}")
def delete_document(doc_id: str):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM documents WHERE id = %s", (doc_id,))
            return {"status": "deleted"}


# Document Store (new module)
# -----------------------------------------------------------------------------

store = get_store_repo()


@app.get("/store")
def store_status():
    return {"store_backend": store.__class__.__name__}


@app.post("/store/documents")
def store_create_document(doc: StoreDocumentCreate):
    return store.create(doc.model_dump())


@app.get("/store/documents")
def store_list_documents(limit: int = 50):
    return store.list(limit=limit)


@app.get("/store/documents/{doc_id}")
def store_get_document(doc_id: str):
    d = store.get(doc_id)
    if d is None:
        raise HTTPException(status_code=404, detail="Store document not found")
    return d


@app.patch("/store/documents/{doc_id}")
def store_update_document(doc_id: str, patch: StoreDocumentUpdate):
    d = store.update(doc_id, patch.model_dump())
    if d is None:
        raise HTTPException(status_code=404, detail="Store document not found")
    return d


@app.delete("/store/documents/{doc_id}")
def store_delete_document(doc_id: str):
    ok = store.delete(doc_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Store document not found")
    return {"status": "deleted"}


@app.get("/store/documents/search")
def store_search(q: str | None = None, tag: str | None = None, source: str | None = None, limit: int = 50):
    return store.search(q=q, tag=tag, source=source, limit=limit)
