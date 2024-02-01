from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
from models import Question

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list", response_model=list[question_schema.Question])
def quesiton_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

