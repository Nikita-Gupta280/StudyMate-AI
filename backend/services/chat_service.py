from services.rag_pipeline import ask


def get_chat_response(question: str):
    result = ask(question)
    return result["answer"]