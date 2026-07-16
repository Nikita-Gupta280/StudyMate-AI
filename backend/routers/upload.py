from fastapi import APIRouter, UploadFile, File
import shutil
import os

from services.ingest import ingest_file
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_result = ingest_file(file_path)

    return {
        "message": "File uploaded successfully!",
        "ingestion": ingest_result
    }