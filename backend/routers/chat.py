from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import get_chat_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    answer = get_chat_response(request.question)
    return {
        "question": request.question,
        "answer": answer
    }