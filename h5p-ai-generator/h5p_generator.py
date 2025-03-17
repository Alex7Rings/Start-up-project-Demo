import json
import os

def generate_h5p_json(question, correct_answer, wrong_answers, filename="quiz.json"):
    """Генерира JSON файл във формат H5P"""
    
    data = {
        "question": question,
        "answers": [
            {"text": correct_answer, "correct": True}
        ] + [{"text": ans, "correct": False} for ans in wrong_answers]
    }

    os.makedirs("generated_h5p", exist_ok=True)
    file_path = os.path.join("generated_h5p", filename)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ H5P JSON файлът е създаден: {file_path}")

if __name__ == "__main__":
    generate_h5p_json("Каква е скоростта на светлината?", "300,000 km/s", ["150,000 km/s", "3,000 km/s"])
