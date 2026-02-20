from __future__ import annotations

import requests
import streamlit as st
import os

API_BASE = os.getenv("API_BASE", "http://localhost:8000")

# API_BASE = st.secrets.get("API_BASE", "http://localhost:8000")

st.set_page_config(page_title="RAG Lab", layout="wide")

st.title("RAG Lab: Postgres + Document Store")

pg_tab, store_tab = st.tabs(["Postgres (relational)", "Store (Mongo/TinyDB)"])


# ---------------------------
# Postgres tab
# ---------------------------

with pg_tab:
    st.subheader("Create Postgres document")
    title = st.text_input("Title", key="pg_title")
    source = st.text_input("Source (optional)", key="pg_source")

    if st.button("Create (Postgres)"):
        r = requests.post(f"{API_BASE}/documents", json={"title": title, "source": source or None})
        st.write(r.status_code)
        st.json(r.json())

    st.subheader("Recent Postgres documents")
    if st.button("Refresh (Postgres)"):
        pass

    r = requests.get(f"{API_BASE}/documents")
    if r.ok:
        st.json(r.json())
    else:
        st.error(r.text)


# ---------------------------
# Store tab
# ---------------------------

with store_tab:
    st.subheader("Create store document")
    title = st.text_input("Title", key="s_title")
    source = st.text_input("Source (optional)", key="s_source")
    content = st.text_area("Content (optional)", key="s_content", height=150)
    tags = st.text_input("Tags (comma-separated)", key="s_tags")

    if st.button("Create (Store)"):
        payload = {
            "title": title,
            "source": source or None,
            "content": content or None,
            "tags": [t.strip() for t in tags.split(",") if t.strip()],
        }
        r = requests.post(f"{API_BASE}/store/documents", json=payload)
        st.write(r.status_code)
        st.json(r.json())

    st.subheader("Search store documents")
    q = st.text_input("Contains text (q)", key="s_q")
    tag = st.text_input("Tag (exact match)", key="s_tag")
    src = st.text_input("Source (exact match)", key="s_src")

    r = requests.get(
        f"{API_BASE}/store/documents/search",
        params={"q": q or None, "tag": tag or None, "source": src or None, "limit": 50},
    )
    if r.ok:
        st.json(r.json())
    else:
        st.error(r.text)
