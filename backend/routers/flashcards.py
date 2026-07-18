from fastapi import APIRouter
from services.flashcard_service import get_flashcards

router = APIRouter()


@router.post("/flashcards")
def generate_flashcards():
    return get_flashcards()