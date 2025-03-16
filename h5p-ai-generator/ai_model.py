import openai

API_KEY = "YOUR_OPENAI_API_KEY"

def generate_question(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(generate_question("Генерирай въпрос за физика"))
