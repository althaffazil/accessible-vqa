def normalize_question(question: str):
    question = question.strip()
    if not question.endswith("?"):
        question += "?"
    return question
