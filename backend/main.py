from fastapi import FastAPI
from routers.upload import router as upload_router
from routers.files import router as files_router
from routers.chat import router as chat_router
from routers.quiz import router as quiz_router
from routers.flashcards import router as flashcards_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(files_router)
app.include_router(chat_router)
app.include_router(quiz_router)
app.include_router(flashcards_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to StudyMate AI Backend!"
    }