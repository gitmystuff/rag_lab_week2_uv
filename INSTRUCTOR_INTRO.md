# Instructor guide (first 30 minutes)

Timebox these sections. The goal is to get students building quickly.

## 0:00–0:05  Welcome + recap

- Last month: Postgres + FastAPI CRUD.
- Today: keep those endpoints **unchanged**, and add a **document store** next to Postgres.
- This mirrors real systems: one service can talk to multiple persistence layers.

## 0:05–0:15  Terms and concepts

Use these terms consistently.

- Relational (Postgres)
  - Table, row, column, schema, primary key
  - Good for transactional, structured data
- Document store (MongoDB / TinyDB)
  - Collection, document (JSON-like), flexible schema
  - Good for semi-structured content (notes, web pages, transcripts)
- IDs
  - Postgres uses integer IDs (today)
  - Store uses a stable **string UUID** `id` (works for Mongo and TinyDB)
  - That string `id` becomes your cross-system key later (ChromaDB + Neo4j)

## 0:15–0:25  Architecture for the semester (light, practical)

Draw this on the board:

- Postgres: system-of-record metadata (users, audit, pipelines, assignment tracking)
- Document store: content objects (documents you will embed later)
- ChromaDB: embeddings + similarity search
- Neo4j: entities + relationships + provenance

Emphasize separation of concerns:

- API stays stable
- Storage can change

## 0:25–0:30  What students will build today

- Confirm Postgres endpoints still run: `/documents`
- Add store endpoints: `/store/documents` (Mongo or TinyDB)
- Add one search endpoint: `/store/documents/search`
- Build a Streamlit UI to call both

Then transition into the code-along:

- Everyone runs the smoke test notebook
- Everyone starts the FastAPI server
- Everyone hits `/docs`
