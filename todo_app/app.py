from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_all_cards, create_card, update_card_status

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', cards=get_all_cards())

@app.route('/create', methods = ['POST'])
def create():
    new_card_title = request.form.get('card-title')
    create_card(new_card_title)
    return redirect(url_for('index'))

@app.route('/update', methods = ['POST'])
def update():
    card_id = request.form.get('card-id')
    card_status = request.form.get('card-status')
    update_card_status(card_id, card_status)
    return redirect(url_for('index'))