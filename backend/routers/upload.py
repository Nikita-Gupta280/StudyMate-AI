from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
def upload_page():
    return {
        "message": "Upload API is working!"
    }