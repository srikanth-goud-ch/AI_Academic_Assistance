from fastapi import APIRouter, UploadFile
import shutil
from app.rag.ingest import ingest_pdf

router = APIRouter()

@router.post("/")
def upload(file: UploadFile):
    path = f"temp_{file.filename}"
    
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(path, metadata={"source": file.filename})

    return {"message": "Uploaded & processed"}