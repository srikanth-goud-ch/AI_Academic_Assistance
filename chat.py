from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.pipeline import run_rag

router = APIRouter()

class Query(BaseModel):
    question: str
    course: str | None = None
    year: str | None = None

@router.post("/")
def chat(query: Query):
    filters = {"course": query.course, "year": query.year}
    return run_rag(query.question, filters)