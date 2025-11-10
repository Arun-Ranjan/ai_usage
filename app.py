from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Load benchmarks data
with open('benchmarks.json', 'r') as f:
    benchmarks = json.load(f)

TASKS = {
    "code_review": "Code Review",
    "code_summarization": "Code Summarization",
    "bug_detection": "Bug Detection",
    "code_qa": "Code Q&A"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_task = request.form.get('task') if request.method == 'POST' else 'code_review'
    bench = benchmarks[selected_task]
    return render_template(
        'index.html',
        tasks=TASKS,
        selected_task=selected_task,
        bench=bench
    )

if __name__ == '__main__':
    app.run(debug=True)