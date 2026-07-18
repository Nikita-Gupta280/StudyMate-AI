from fastapi import APIRouter
from services.quiz_service import get_quiz

router = APIRouter()


@router.post("/quiz")
def generate_quiz():
    return get_quiz()