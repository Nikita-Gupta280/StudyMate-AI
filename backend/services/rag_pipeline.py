"""
StudyMate AI - RAG Query Pipeline
Retrieves relevant chunks from ChromaDB and generates an answer using
Groq, with per-session conversation memory.

This is the module Nikita's FastAPI /chat endpoint should import and call.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory

CHROMA_DIR = "chroma_db"

# In-memory session store: {session_id: chain}.
# Fine for a demo/capstone. For production, swap for a persisted store.
_sessions = {}

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


def get_vectordb(collection_name: str = "studymate"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )


def get_llm():
    key = os.getenv("GROQ_API_KEY")
    print("API KEY FOUND:", key is not None)
    if key:
        print("API KEY PREFIX:", key[:8])

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=key,
    )


def get_chain(session_id: str, collection_name: str = "studymate"):
    if session_id not in _sessions:
        vectordb = get_vectordb(collection_name)
        retriever = vectordb.as_retriever(search_kwargs={"k": 4})
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
        )
        chain = ConversationalRetrievalChain.from_llm(
            llm=get_llm(),
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
        )
        _sessions[session_id] = chain
    return _sessions[session_id]


def ask(question: str, session_id: str = "default", collection_name: str = "studymate"):
    """
    Main entry point. Call this from the backend's /chat endpoint.

    Returns: {"answer": str, "sources": [filenames]}
    """
    chain = get_chain(session_id, collection_name)
    result = chain.invoke({"question": question})
    sources = list({
        doc.metadata.get("source", "unknown")
        for doc in result.get("source_documents", [])
    })
    return {
        "answer": result["answer"],
        "sources": sources,
    }


if __name__ == "__main__":
    print(ask("Explain Newton's Second Law."))
    print(ask("Give one real-world example of it."))
