import openai

openai_client = openai.OpenAI()  # Create OpenAI client

def generate_question(topic, difficulty="Medium", q_type="Multiple Choice"):
    prompt = f"Generate a {difficulty} {q_type} question about {topic}."
    
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
