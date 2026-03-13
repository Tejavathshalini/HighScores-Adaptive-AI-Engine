from app.database import questions_collection


def seed_questions():

    questions = [

{"question":"What is 15% of 200?","options":["25","30","35","40"],"correct_answer":"30","difficulty":0.2,"topic":"Arithmetic","tags":["percentage"]},

{"question":"Solve: 2x + 5 = 15","options":["3","5","10","7"],"correct_answer":"5","difficulty":0.3,"topic":"Algebra","tags":["equation"]},

{"question":"What is 7 * 8?","options":["54","56","48","64"],"correct_answer":"56","difficulty":0.1,"topic":"Arithmetic","tags":["multiplication"]},

{"question":"Square root of 144?","options":["10","11","12","13"],"correct_answer":"12","difficulty":0.2,"topic":"Arithmetic","tags":["square root"]},

{"question":"Synonym of Rapid?","options":["Slow","Fast","Late","Weak"],"correct_answer":"Fast","difficulty":0.4,"topic":"Vocabulary","tags":["english"]},

{"question":"Solve: 3x = 12","options":["2","3","4","6"],"correct_answer":"4","difficulty":0.3,"topic":"Algebra","tags":["equation"]},

{"question":"What is 20% of 150?","options":["20","30","25","35"],"correct_answer":"30","difficulty":0.2,"topic":"Arithmetic","tags":["percentage"]},

{"question":"5^2 = ?","options":["10","15","20","25"],"correct_answer":"25","difficulty":0.2,"topic":"Arithmetic","tags":["power"]},

{"question":"Solve: x + 8 = 20","options":["10","11","12","13"],"correct_answer":"12","difficulty":0.3,"topic":"Algebra","tags":["equation"]},

{"question":"What is 9 * 9?","options":["72","81","90","99"],"correct_answer":"81","difficulty":0.2,"topic":"Arithmetic","tags":["multiplication"]},

{"question":"Antonym of 'Hot'?","options":["Cold","Warm","Heat","Sun"],"correct_answer":"Cold","difficulty":0.3,"topic":"Vocabulary","tags":["english"]},

{"question":"Solve: 4x + 2 = 18","options":["3","4","5","6"],"correct_answer":"4","difficulty":0.5,"topic":"Algebra","tags":["equation"]},

{"question":"25% of 80?","options":["10","15","20","25"],"correct_answer":"20","difficulty":0.2,"topic":"Arithmetic","tags":["percentage"]},

{"question":"Cube of 3?","options":["6","9","27","18"],"correct_answer":"27","difficulty":0.4,"topic":"Arithmetic","tags":["power"]},

{"question":"Solve: 10x = 100","options":["5","10","15","20"],"correct_answer":"10","difficulty":0.3,"topic":"Algebra","tags":["equation"]},

{"question":"Opposite of 'Strong'?","options":["Weak","Hard","Heavy","Large"],"correct_answer":"Weak","difficulty":0.3,"topic":"Vocabulary","tags":["english"]},

{"question":"What is 12 * 12?","options":["124","144","134","154"],"correct_answer":"144","difficulty":0.3,"topic":"Arithmetic","tags":["multiplication"]},

{"question":"Solve: x/2 = 6","options":["6","8","10","12"],"correct_answer":"12","difficulty":0.4,"topic":"Algebra","tags":["equation"]},

{"question":"10% of 500?","options":["40","50","60","70"],"correct_answer":"50","difficulty":0.2,"topic":"Arithmetic","tags":["percentage"]},

{"question":"Synonym of 'Happy'?","options":["Sad","Joyful","Angry","Weak"],"correct_answer":"Joyful","difficulty":0.3,"topic":"Vocabulary","tags":["english"]}

]

    result = questions_collection.insert_many(questions)

    print(f"{len(result.inserted_ids)} questions inserted successfully")


if __name__ == "__main__":
    seed_questions()