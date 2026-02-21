# Student Guide: Postgres + Document Store (MongoDB or TinyDB)

## Overview

You will:

* Keep your existing **Postgres API working**
* Add and verify a **Document Store API** using MongoDB (preferred) or TinyDB (fallback)
* Extend your API and Streamlit UI
* Create and verify documents in both databases
* Submit screenshots as proof

---

# What You Should Have When Finished

## Postgres Endpoints (already built)

* `POST /documents`
* `GET /documents`
* `GET /documents/{doc_id}`
* `DELETE /documents/{doc_id}`

## Store Endpoints (verify and extend today)

* `POST /store/documents`
* `GET /store/documents`
* `GET /store/documents/{doc_id}`
* `PATCH /store/documents/{doc_id}` ← implement if missing
* `DELETE /store/documents/{doc_id}`
* `GET /store/documents/search?q=...` ← implement if missing

Store backend:

* MongoDB (preferred)
* TinyDB (fallback)

---

# Step 1 — Setup Environment

From the project folder:

Install dependencies:

```
uv sync
```

Run applications:

FastAPI:

```
uv run uvicorn app.main:app --reload
```

Streamlit:

```
uv run streamlit run streamlit_app.py
```

Notebook (optional):

```
uv run jupyter notebook
```

---

# Step 2 — Choose Store Backend

& "C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres

If you need to find what version (e.g. 17) you are using - Get-ChildItem -Path "C:\Program Files\PostgreSQL" -Recurse -Filter "psql.exe"

list databases - \l

Create database - CREATE DATABASE rag_lab;

Verify - \l

Use rag_lab - \c rag_lab

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

\dt

\q

uv run uvicorn app.main:app –reload

make sure db.py has the correct credentials

Edit `.env`

## Option A — MongoDB (Preferred)

Make sure MongoDB is running, then:

```
STORE_BACKEND=mongo
MONGO_URL=mongodb://localhost:27017
```

## Option B — TinyDB (Fallback)

```
STORE_BACKEND=tinydb
```

---

# Step 3 — Run Smoke Test Notebook (Recommended)

Install notebook:

uv sync --extra notebook 

Start notebook:

uv run jupyter notebook

Open:

```
notebook/00_store_smoke_test.ipynb
```

Run all cells.

Verify:

* Create works
* List works
* Update works
* Delete works

If MongoDB does not work, switch to TinyDB.

---

# Step 4 — Start FastAPI

Start server:

```
uv run uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

# Step 5 — Verify Postgres Still Works (Review)

In Swagger:

Test:

```
POST /documents
GET /documents
```

If Postgres is not working, complete the Store portion first and fix Postgres later.

---

# Step 6 — Verify Store CRUD Works

In Swagger:

Create:

```
POST /store/documents
```

Example:

```json
{
  "title": "Test Document",
  "source": "class",
  "content": "This is a test.",
  "tags": ["demo"]
}
```

Verify:

```
GET /store/documents
GET /store/documents/{doc_id}
DELETE /store/documents/{doc_id}
```

---

# Step 7 — Implement Update Endpoint (if not already implemented)

Add:

```
PATCH /store/documents/{doc_id}
```

Requirements:

* Updates title/content/tags
* Returns updated document
* Returns 404 if document not found

Test in Swagger.

---

# Step 8 — Implement Search Endpoint (if not already implemented)

Add:

```
GET /store/documents/search?q=...
```

Requirements:

TinyDB:

* Simple substring match

MongoDB:

* Field search or regex

Test in Swagger.

---

# Step 9 — Update Streamlit UI

Run:

```
uv run streamlit run streamlit_app.py
```

Add support for:

* View documents
* Update documents
* Search documents

Important:

Streamlit must call FastAPI only.

Do NOT access databases directly from Streamlit.

---

# Step 10 — Create and Verify Documents (REQUIRED)

You must create documents in BOTH Postgres and MongoDB.

---

# Step 11 — Create 5 Postgres Documents

Open:

```
http://localhost:8000/docs
```

Use:

```
POST /documents
```

Create 5 documents.

Example:

```json
{
  "title": "Postgres YourName Doc 1",
  "content": "Stored in Postgres"
}
```

---

# Step 12 — Verify Postgres Documents

Use:

```
GET /documents
```

Confirm all 5 appear.

---

# Step 13 — Screenshot Postgres Results

Screenshot must show:

* Swagger page
* GET /documents endpoint
* All 5 documents visible

---

# Step 14 — Create 5 MongoDB Documents

Use:

```
POST /store/documents
```

Example:

```json
{
  "title": "Mongo YourName Doc 1",
  "content": "Stored in MongoDB"
}
```

Create 5 documents.

---

# Step 15 — Verify MongoDB Documents

Use:

```
GET /store/documents
```

Confirm all 5 appear.

---

# Step 16 — Screenshot MongoDB Results

Screenshot must show:

* Swagger page
* GET /store/documents endpoint
* All 5 documents visible

---

# Optional Bonus (Recommended)

Open MongoDB Compass.

Verify:

```
rag_lab
└── store_documents
```

Take screenshot.

---

# Why This Matters

You are using two database types:

Postgres:

* Relational
* Structured schema

MongoDB:

* Document-based
* Flexible schema

This is a common architecture in modern AI systems.

---

# Submission Instructions

Create a Word document named:

```
YourName_RagLab_2.docx
```

Include:

* Screenshot of Postgres documents
* Screenshot of MongoDB documents

Submit:

* Shared link with View access
* Updated code in GitHub

---

# Naming Requirement (Important)

Postgres:

```
Postgres YourName Doc 1
```

Mongo:

```
Mongo YourName Doc 1
```

This confirms your work is original.

---

# You are done when:

You can:

* Create documents in Postgres
* Create documents in MongoDB
* Update store documents
* Search store documents
* View documents in Streamlit
