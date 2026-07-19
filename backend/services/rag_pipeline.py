"""
StudyMate AI - RAG Query Pipeline
Retrieves relevant chunks from ChromaDB and generates an answer using
Groq, with per-session conversation memory.

This is the module Nikita's FastAPI /chat endpoint should import and call.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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


    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=key,
    )

QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are StudyMate AI, a friendly AI tutor.

You MUST answer ONLY from the provided study material.

If the answer is not present, say:
"I couldn't find this information in your uploaded notes."

When answering:

1. Give a simple explanation.
2. If possible, give a real-life example.
3. Mention important exam points.
4. Keep the answer well formatted using headings.
5. Never invent facts.

Study Material:
{context}

Student Question:
{question}

Answer:
"""
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
            combine_docs_chain_kwargs={
                "prompt": QA_PROMPT
},
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

def generate_from_notes(
    instruction: str,
    session_id: str = "default",
    collection_name: str = "studymate",
):
    vectordb = get_vectordb(collection_name)
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    docs = retriever.invoke(instruction)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are StudyMate AI.

Use ONLY the study material below.

Study Material:
{context}

Task:
{instruction}
"""

    response = get_llm().invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            doc.metadata.get("source", "unknown")
            for doc in docs
        ]
    }

def generate_quiz(session_id: str = "default", collection_name: str = "studymate"):
    """
    Generates a quiz from the uploaded study material.
    """

    prompt = """
    Using ONLY the uploaded study material, generate exactly 5 multiple-choice questions.

    IMPORTANT FORMATTING RULES:

    - Return the output in Markdown.
    - Put each option on a NEW LINE.
    - Leave one blank line after every question.
    - Leave one blank line before the explanation.
 
    Example:
 
    ## Q1. Question
 
    A. Option A
 
    B. Option B
 
    C. Option C
 
    D. Option D
  
    **Correct Answer:** B
 
    **Explanation:** Explain why B is correct.
 
    Repeat this format for all 5 questions.
 
    Do NOT invent information.
    Use ONLY the uploaded study material.
    """

    return generate_from_notes(
        instruction=prompt,
        session_id=session_id,
        collection_name=collection_name,
    )
def generate_flashcards(session_id: str = "default", collection_name: str = "studymate"):
        """
        Generates flashcards from the uploaded study material.
        """

        prompt = """
        Using ONLY the uploaded study material, generate exactly 10 flashcards.

        Return them in this format:

        Flashcard 1
        Front: ...
        Back: ...

        Flashcard 2
        Front: ...
        Back: ...

        Continue until Flashcard 10.

        Do NOT invent information.
        Use only the uploaded notes.
        """

        return generate_from_notes(
            instruction=prompt,
            session_id=session_id,
            collection_name=collection_name,
      )
        


if __name__ == "__main__":
    print(ask("Explain Newton's Second Law."))
    print(ask("Give one real-world example of it."))

    