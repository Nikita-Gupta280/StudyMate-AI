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
# Load the embedding model only once
EMBEDDINGS = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# In-memory session store: {session_id: chain}.
# Fine for a demo/capstone. For production, swap for a persisted store.
_sessions = {}

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


def get_vectordb(collection_name: str = "studymate"):
    return Chroma(
        collection_name=collection_name,
        embedding_function=EMBEDDINGS,
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
You are StudyMate AI, an intelligent and adaptive study assistant. Tailor your response style to the student's request instead of following a fixed template.

You MUST answer ONLY from the provided study material.

If the answer is not present, say:
"I couldn't find this information in your uploaded notes."

When answering:

- Answer according to the student's question.
- Format each response naturally instead of using the same template.
- Use headings only when they improve readability.
- Use bullet points, numbered lists, tables, or short paragraphs when appropriate.
- Give a real-life example only if it helps explain the concept.
- Mention exam tips only when they are relevant.
- Avoid repetitive introductions like "Introduction", "Key Points", or "Important Exam Points" unless the question specifically asks for them.
- Keep the answer concise but complete.
- Never invent facts.

Study Material:
{context}

Student Question:
{question}

Answer:
"""
)

import time   # Add this at the top of the file if it's not already there

def get_chain(session_id: str, collection_name: str = "studymate"):
    if session_id not in _sessions:

        start = time.time()
        vectordb = get_vectordb(collection_name)
        print(f"✅ VectorDB loaded in {time.time() - start:.2f} sec")

        start = time.time()
        retriever = vectordb.as_retriever(search_kwargs={"k": 4})
        print(f"✅ Retriever created in {time.time() - start:.2f} sec")

        start = time.time()
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

        print(f"✅ Chain created in {time.time() - start:.2f} sec")

        _sessions[session_id] = chain

    return _sessions[session_id]

import time
def ask(question: str, session_id: str = "default", collection_name: str = "studymate"):
    """
    Main entry point. Call this from the backend's /chat endpoint.

    Returns: {"answer": str, "sources": [filenames]}
    """
     

    chain = get_chain(session_id, collection_name)

    start = time.time()
    result = chain.invoke({"question": question})
    print(f"✅ LLM response took {time.time() - start:.2f} seconds")
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

    print("\n========== RETRIEVED SOURCES ==========")

    for doc in docs:
        print(doc.metadata.get("source"))

    print("======================================\n")

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

    Follow these rules STRICTLY:

    # 📝 AI Quiz

    - Return the output in proper Markdown.
    - Generate exactly 5 questions.
    - Each question must have exactly 4 options.
    - Put every option on a separate line.
    - Leave one blank line between sections.
    - Add a horizontal separator (---) after every question.
    - Do NOT use tables.
    - Do NOT invent information.
    - Use ONLY the uploaded study material.

    Use this exact format:

    # 📝 AI Quiz

    ## Question 1

    Question text here?

    A. Option A

    B. Option B

    C. Option C

    D. Option D

    ✅ **Correct Answer:** B

    💡 **Explanation:**
    Write a short explanation (1–2 sentences).

    ---

    Repeat this format for Questions 2, 3, 4 and 5.
    """

    return generate_from_notes(
        instruction=prompt,
        session_id=session_id,
        collection_name=collection_name,
    )
def generate_flashcards(session_id: str = "default", collection_name: str = "studymate"):
    print("🔥 GENERATE_FLASHCARDS FUNCTION CALLED")
    """
    Generates flashcards from the uploaded study material.
    """

    prompt = """
Using ONLY the uploaded study material, generate exactly 5 flashcards.

Follow these rules STRICTLY:

# 🧠 AI Flashcards

- Return the output in proper Markdown.
- Generate exactly 5 flashcards.
- Each flashcard should test one important concept.
- Keep the Front short (one question).
- Keep the Back clear and educational (2–3 sentences).
- Leave one blank line between sections.
- Add a horizontal separator (---) after every flashcard.
- Do NOT use tables.
- Do NOT invent information.
- Use ONLY the uploaded study material.

Use this exact format:

# 🧠 AI Flashcards

## 🧠 Flashcard 1

### Front

What is the concept?

### Back

Answer the question in 2–3 sentences.

---

## 🧠 Flashcard 2

### Front

Question

### Back

Answer

---

Continue until Flashcard 5.
"""

    return generate_from_notes(
        instruction=prompt,
        session_id=session_id,
        collection_name=collection_name,
    )