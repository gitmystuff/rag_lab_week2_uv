# Student guide: Postgres + Document Store (MongoDB or TinyDB)

You will keep last month’s Postgres API working, and add a document store alongside it.

## What you will build

- Postgres endpoints (already built)
  - `POST /documents`
  - `GET /documents`
  - `GET /documents/{doc_id}`
  - `DELETE /documents/{doc_id}`

- Store endpoints (you will build/verify today)
  - `POST /store/documents`
  - `GET /store/documents`
  - `GET /store/documents/{doc_id}`
  - `PATCH /store/documents/{doc_id}`
  - `DELETE /store/documents/{doc_id}`
  - `GET /store/documents/search?q=...&tag=...&source=...`

The store backend is either:

- MongoDB (preferred if you have it installed and running)
- TinyDB (fallback if you do not)

## 1) Setup with uv

From the project folder:

1. Install dependencies

- `uv sync`

2. Run everything inside uv

- FastAPI: `uv run uvicorn app.main:app --reload`
- Streamlit: `uv run streamlit run streamlit_app.py`
- Notebook (optional): `uv run jupyter notebook`

## 2) Choose a store backend

### Option A: TinyDB (works for everyone)

Set:

- `STORE_BACKEND=tinydb`

This stores documents in a local file `tinydb.json`.

### Option B: MongoDB (if installed)

Start MongoDB locally, then set:

- `STORE_BACKEND=mongo`
- `MONGO_URL=mongodb://localhost:27017`

## 3) Run the smoke test notebook (recommended)

Open the notebook:

- `notebook/00_store_smoke_test.ipynb`

Run all cells.

Check:

- You can create a document
- You can list documents
- You can update and delete

If you cannot get MongoDB working, switch to TinyDB and continue.

## 4) Start the API

- `uv run uvicorn app.main:app --reload`

Open:

- `http://localhost:8000/docs`

## 5) Verify Postgres endpoints still work (review)

Try `POST /documents` in Swagger.

Then `GET /documents`.

If Postgres is not running, you can still complete the store portion today.

## 6) Verify store endpoints

In Swagger (`/docs`):

1. Create a store document

- `POST /store/documents`

Use JSON like:

```json
{
  "title": "Mongo vs TinyDB",
  "source": "class",
  "content": "This is a note.",
  "tags": ["demo", "notes"]
}
```

2. List

- `GET /store/documents`

3. Get by id

- `GET /store/documents/{doc_id}`

4. Update

- `PATCH /store/documents/{doc_id}`

Example patch:

```json
{
  "content": "Updated content",
  "tags": ["demo", "updated"]
}
```

5. Search

- `GET /store/documents/search?q=updated`

## 7) Run the Streamlit app

- `uv run streamlit run streamlit_app.py`

In the UI:

- Create and list Postgres documents (if Postgres is running)
- Create and search store documents

## 8) What to submit

- A screenshot of Swagger showing store endpoints working
- A screenshot of Streamlit showing store search results
- A short note (5–8 sentences):
  - When would you store something in Postgres vs the document store?
  - What fields would you add to store documents to prepare for embeddings next month?
