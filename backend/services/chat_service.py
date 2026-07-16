from services.rag_pipeline import ask


def get_chat_response(question: str):
    return ask(question)