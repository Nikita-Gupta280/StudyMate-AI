from fastapi import APIRouter, UploadFile, File
import shutil
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
   with open(f"uploads/{file.filename}", "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

   return {"message": "File uploaded successfully!"}