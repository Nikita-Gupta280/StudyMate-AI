"""
StudyMate AI - Ingestion Pipeline
Loads a document, chunks it, embeds it (locally), and stores it in ChromaDB.

Usage:
    python ingest.py path/to/notes.pdf
"""

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from document_loader import load_document

CHROMA_DIR = "chroma_db"


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def chunk_text(text: str, source: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )
    return splitter.create_documents([text], metadatas=[{"source": source}])


def ingest_file(file_path: str, collection_name: str = "studymate"):
    """
    Full pipeline: extract -> chunk -> embed -> store.

    collection_name lets you keep materials separate per student
    or per subject (Nikita's backend can pass a student/session ID here).
    """
    text = load_document(file_path)
    if not text.strip():
        raise ValueError(f"No extractable text found in {file_path}")

    source_name = os.path.basename(file_path)
    docs = chunk_text(text, source_name)

    embeddings = get_embeddings()
    vectordb = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    vectordb.add_documents(docs)
    vectordb.persist()

    return {"file": source_name, "chunks_added": len(docs)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <file_path>")
        sys.exit(1)
    result = ingest_file(sys.argv[1])
    print(result)
