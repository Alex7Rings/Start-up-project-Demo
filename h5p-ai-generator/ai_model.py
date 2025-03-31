import openai
import os

# Get API key from environment variable OR set it directly
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

# Create OpenAI client with API key
openai_client = openai.OpenAI(api_key=api_key)

def generate_question(topic, difficulty="Medium", q_type="Multiple Choice"):
    prompt = f"Generate a {difficulty} {q_type} question about {topic}."
    
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
