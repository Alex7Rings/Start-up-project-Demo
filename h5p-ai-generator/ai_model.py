import openai

openai_client = openai.OpenAI()  # Create OpenAI client

def generate_question(topic):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Generate a question about {topic}"}]
    )
    return response.choices[0].message.content
