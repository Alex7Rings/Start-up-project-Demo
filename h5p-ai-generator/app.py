from flask import Flask, render_template, request, send_file
from ai_model import generate_question
from h5p_generator import generate_h5p_json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    question = ""
    if request.method == "POST":
        topic = request.form["topic"]
        question = generate_question(topic)

    return render_template("index.html", question=question)

@app.route("/generate", methods=["POST"])
def generate():
    question = request.form["question"]
    correct_answer = request.form["correct_answer"]
    wrong_answers = request.form["wrong_answers"].split(",")

    file_path = generate_h5p_json(question, correct_answer, wrong_answers)

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
