def generate_study_plan(ability: float):

    if ability < 0.3:
        level = "Beginner"
        recommendations = [
            "Practice basic arithmetic",
            "Review algebra fundamentals",
            "Improve vocabulary"
        ]

    elif ability < 0.7:
        level = "Intermediate"
        recommendations = [
            "Practice algebra problems",
            "Solve word problems",
            "Improve calculation speed"
        ]

    else:
        level = "Advanced"
        recommendations = [
            "Practice GRE mock tests",
            "Focus on weak topics",
            "Solve timed quizzes"
        ]

    return {
        "level": level,
        "recommendations": recommendations
    }