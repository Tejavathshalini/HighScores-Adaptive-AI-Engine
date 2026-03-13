from app.database import db

sessions_collection = db["user_sessions"]

def create_session():
    session = {
        "ability": 0.5,
        "questions_answered": 0,
        "correct_answers": 0
    }

    result = sessions_collection.insert_one(session)
    return str(result.inserted_id)


def update_session(session_id, correct):
    session = sessions_collection.find_one({"_id": session_id})

    ability = session["ability"]

    if correct:
        ability += 0.1
    else:
        ability -= 0.1

    ability = max(0.1, min(1.0, ability))

    sessions_collection.update_one(
        {"_id": session_id},
        {
            "$set": {"ability": ability},
            "$inc": {"questions_answered": 1},
            "$inc": {"correct_answers": 1 if correct else 0}
        }
    )

    return ability