import openai

API_KEY = "YOUR_OPENAI_API_KEY"  # Замени с твоя OpenAI API ключ

def generate_question(topic):
    """Генерира въпрос на база на дадена тема."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Генерирай въпрос за {topic}"}]
    )
    return response["choices"][0]["message"]["content"]
