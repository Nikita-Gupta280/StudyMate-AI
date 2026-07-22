from fastapi import APIRouter, UploadFile, File
import shutil

from services.ingest import ingest_file
from services.rag_pipeline import _sessions

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_result = ingest_file(file_path)

    # Clear old chat sessions after uploading a new document
    _sessions.clear()

    return {
        "message": f"{file.filename} uploaded successfully!",
        "ingestion": ingest_result
    }