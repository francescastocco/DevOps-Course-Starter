from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    tasks = get_items()
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    newTaskTitle = request.form.get('task-title')
    add_item(newTaskTitle)
    return redirect(url_for('index'))