"""Create a persistent Chroma database with an empty collection."""

from pathlib import Path

import chromadb

DB_PATH = Path(__file__).resolve().parent / "chroma_data"
COLLECTION_NAME = "documents"


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    print(f"Chroma database: {DB_PATH}")
    print(f"Collection: {collection.name}")
    print(f"Documents: {collection.count()}")


if __name__ == "__main__":
    main()
