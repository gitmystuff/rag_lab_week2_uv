INFO 5707 — Data Modeling

Starter: Postgres CRUD (Week 1) + Document Store CRUD (Week 2)

What you get

- Postgres schema in `sql/schema.sql` (Week 1)
- FastAPI app in `app/main.py`
  - Postgres endpoints under `/documents`
  - Document store endpoints under `/store/documents`
- Postgres connection helper in `app/db.py` (edit only your password)
- Store backend selection via env vars (MongoDB or TinyDB fallback)
- Streamlit UI in `streamlit_app.py`
- Smoke test notebook in `notebook/00_store_smoke_test.ipynb`
- Step-by-step student instructions in `STUDENT_GUIDE.md`

Prerequisites

- Python 3.10+
- uv installed (recommended)
- Postgres installed locally and running (for Week 1 endpoints)
- MongoDB installed locally (optional; TinyDB fallback is provided)

Setup with uv (recommended)

1) Install dependencies

  uv sync

2) Run the API

  uv run uvicorn app.main:app --reload

3) Test in Swagger

  http://127.0.0.1:8000/docs

4) Run the Streamlit app

  uv run streamlit run streamlit_app.py

Store backend selection

- TinyDB (works for everyone)
  - `STORE_BACKEND=tinydb`
  - stores documents in `tinydb.json`

- MongoDB (if installed)
  - `STORE_BACKEND=mongo`
  - `MONGO_URL=mongodb://localhost:27017`

Postgres setup (Week 1)

1) Create the database (one-time)

Option A (psql):

  psql -U postgres
  CREATE DATABASE rag_lab;
  \q

Option B (pgAdmin):

- Create a database named `rag_lab`

2) Apply the schema

  psql -U postgres -d rag_lab -f sql/schema.sql

3) Set your Postgres password

Open `app/db.py` and replace `YOUR_PASSWORD` with your local postgres password.
(If your username/port are different, update those fields too.)

Endpoints included

Postgres (relational)

- GET /
- POST /documents
- GET /documents
- GET /documents/{doc_id}
- DELETE /documents/{doc_id}

Store (MongoDB or TinyDB)

- GET /store
- POST /store/documents
- GET /store/documents
- GET /store/documents/{doc_id}
- PATCH /store/documents/{doc_id}
- DELETE /store/documents/{doc_id}
- GET /store/documents/search?q=...&tag=...&source=...
