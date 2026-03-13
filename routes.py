from fastapi import APIRouter
from app.database import questions_collection
from app.adaptive_engine import get_next_question
from app.ai_study_plan import generate_study_plan
from app.session import create_session, update_session

router = APIRouter()

@router.get("/questions")
def get_questions():
    return list(questions_collection.find({}, {"_id": 0}))

@router.get("/next-question")
def next_question(ability: float = 0.5):
    return get_next_question(ability)

@router.get("/study-plan")
def get_study_plan(ability: float = 0.5):
    return generate_study_plan(ability)

from fastapi import Body


@router.post("/start-session")
def start_session():
    session_id = create_session()
    return {"session_id": session_id}


@router.post("/submit-answer")
def submit_answer(
    session_id: str = Body(...),
    correct: bool = Body(...)
):
    new_ability = update_session(session_id, correct)

    question = get_next_question(new_ability)

    return {
        "new_ability": new_ability,
        "next_question": question
    }