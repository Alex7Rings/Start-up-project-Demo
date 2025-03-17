from ai_model.py import generate_question
from h5p_generator.py import generate_h5p_json

def main():
    print("🚀 AI H5P Генератор")
    topic = input("🔹 Въведи тема за въпроса: ")

    question = generate_question(f"Генерирай въпрос за {topic}")
    print(f"🧠 AI въпрос: {question}")

    correct_answer = input("✅ Въведи правилния отговор: ")
    wrong_answers = input("❌ Въведи грешни отговори (разделени със запетая): ").split(",")

    generate_h5p_json(question, correct_answer, wrong_answers)

if __name__ == "__main__":
    main()
