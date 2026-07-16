from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import get_chat_response
import traceback

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    try:
        answer = get_chat_response(request.question)
        return {
            "question": request.question,
            "answer": answer
        }
    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }