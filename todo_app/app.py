from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_all_cards, create_card

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    data = get_all_cards()
    return render_template('index.html', lists=data)

@app.route('/create', methods=['POST'])
def create():
    newTaskTitle = request.form.get('task-title')
    create_card(newTaskTitle)
    return redirect(url_for('index'))