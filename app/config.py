import os
from dotenv import load_dotenv

# Load environment variables from a local .env file if present
load_dotenv()

# Store backend: "mongo" (preferred if installed) or "tinydb" (fallback)
STORE_BACKEND = os.getenv("STORE_BACKEND", "tinydb").lower().strip()

# MongoDB connection (only used when STORE_BACKEND=mongo)
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "rag_lab")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "store_documents")

# TinyDB file path (only used when STORE_BACKEND=tinydb)
TINYDB_FILE = os.getenv("TINYDB_FILE", "tinydb.json")
