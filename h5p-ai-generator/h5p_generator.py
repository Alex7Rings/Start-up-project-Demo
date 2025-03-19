import json
import os

def generate_h5p_json(question, correct_answer, wrong_answers):
    """Генерира H5P JSON файл за въпрос с отговори."""
    data = {
        "question": question,
        "answers": [
            {"text": correct_answer, "correct": True}
        ] + [{"text": ans, "correct": False} for ans in wrong_answers]
    }

    os.makedirs("generated_h5p", exist_ok=True)
    file_path = os.path.join("generated_h5p", "quiz.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return file_path
