import random
from app.database import questions_collection

def get_next_question(ability: float):

    # fetch all questions
    questions = list(questions_collection.find({}, {"_id": 0}))

    if not questions:
        return {"message": "No questions found"}

    # find closest difficulty
    closest = min(
        questions,
        key=lambda q: abs(q["difficulty"] - ability)
    )

    return closest