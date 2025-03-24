import openai
import os

# Set your OpenAI API Key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_question(topic, difficulty, q_type):
    prompt = f"""
    Generate a {difficulty} {q_type} question about {topic}.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
