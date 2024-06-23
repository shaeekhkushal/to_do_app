from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime

app = Flask(__name__)

tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = {
        'description': request.form['description'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'completed': False,
        'extra_time': 0
    }
    tasks.append(task)
    return redirect(url_for('index'))


@app.route('/complete_task/<int:task_index>', methods=['POST'])
def complete_task(task_index):
    tasks[task_index]['completed'] = True
    tasks[task_index]['completion_time'] = datetime.datetime.now().strftime("%H:%M")
    return redirect(url_for('index'))


@app.route('/export_data')
def export_data():
    # Implement logic to export tasks to a file or database
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)
