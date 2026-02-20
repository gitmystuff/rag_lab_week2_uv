# Student Guide: Postgres + Document Store (MongoDB or TinyDB)

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

## 8) Create and Verify Documents in Both Databases (Required)

In this step, you will create documents in **Postgres** and **MongoDB**, verify they were saved correctly, and submit screenshots as evidence.

This confirms that your API is correctly connected to both databases.

---

## Step 9 — Create 5 documents in Postgres

Open Swagger:

```
http://localhost:8000/docs
```

Use:

**POST /documents**

Create **five different documents**.

Example:

```json
{
  "title": "Postgres Document 1",
  "content": "This is stored in Postgres"
}
```

Repeat 5 times with different titles.

Example titles:

* Postgres Document 1
* Postgres Document 2
* Postgres Document 3
* Postgres Document 4
* Postgres Document 5

---

## Step 10 — Verify Postgres documents

Use:

**GET /documents**

Confirm you see all 5 documents.

---

## Step 11 — Screenshot Postgres results

Take a screenshot showing:

* Swagger
* GET /documents
* All 5 documents visible

Create a Word document and name it YourName_RagLab_2
Add this screenshot to your file.

---

## Step 12 — Create 5 documents in MongoDB

In Swagger use:

**POST /store/documents**

Example:

```json
{
  "title": "Mongo Document 1",
  "content": "This is stored in MongoDB"
}
```

Create 5 documents.

Example titles:

* Mongo Document 1
* Mongo Document 2
* Mongo Document 3
* Mongo Document 4
* Mongo Document 5

---

## Step 13 — Verify Mongo documents

Use:

**GET /store/documents**

Confirm you see all 5 documents.

---

## Step 14 — Screenshot Mongo results

Take a screenshot showing:

* Swagger
* GET /store/documents
* All 5 Mongo documents visible

Add to your Word file.

---

## Optional Bonus (recommended)

Open MongoDB Compass and verify your collection visually.

Screenshot:

```
rag_lab
└── store_documents
```

---

## Why this step matters

Postgres stores relational data:

• structured schema
• fixed columns

MongoDB stores document data:

• flexible schema
• JSON-like documents

Your system now uses both.

This architecture is common in modern AI systems.

---

## Submission Requirements

Submit:

Confirm the following is in your Word document:

• Screenshot of Postgres documents
• Screenshot of MongoDB documents
• Updated API code
• Updated Streamlit app

Share the document with everyone at UNT with View privileges and submit shared link

---

# Hint: Name Documents Clearly:

Postgres:

```
Postgres StudentName Doc 1
```

Mongo:

```
Mongo StudentName Doc 1
```

