from flask import Flask, render_template, request
import os
from resume_parser import extract_resume_text
from model import predict_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['resume']
        path = "uploads/" + file.filename
        file.save(path)

        text = extract_resume_text(path)
        results = predict_jobs(text)

        return render_template("result.html", results=results)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)