from fastapi import APIRouter, HTTPException
import os

router = APIRouter()


@router.get("/files")
def list_files():
    from fastapi import HTTPException


@router.delete("/files/{filename}")
def delete_file(filename: str):
    file_path = f"uploads/{filename}"

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    os.remove(file_path)

    return {"message": f"{filename} deleted successfully"}
    files = os.listdir("uploads")
    return {"files": files}