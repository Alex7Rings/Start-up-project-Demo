from flask import Flask, render_template, request, jsonify
import json
from ai_model import generate_question
import os

app = Flask(__name__)

# Create a folder to save generated questions
if not os.path.exists('generated_questions'):
    os.makedirs('generated_questions')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data['topic']
    difficulty = data['difficulty']
    q_type = data['question_type']
    
    # Generate question
    question = generate_question(topic, difficulty, q_type)
    
    # Save the question
    save_question(topic, difficulty, q_type, question)
    
    return jsonify({"question": question})


def save_question(topic, difficulty, q_type, question):
    file_path = f'generated_questions/{topic}_questions.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []
    
    data.append({
        "topic": topic,
        "difficulty": difficulty,
        "type": q_type,
        "question": question
    })
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
