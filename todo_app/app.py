from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_all_items, create_item, update_item_status
from todo_app.flask_config import Config
from todo_app.view_models.items_view_model import ItemsViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items_view_model = ItemsViewModel(get_all_items())
        return render_template('index.html', view_model=items_view_model)

    @app.route('/create', methods = ['POST'])
    def create():
        new_item_title = request.form.get('item-title')
        create_item(new_item_title)
        return redirect(url_for('index'))

    @app.route('/update', methods = ['POST'])
    def update():
        item_id = request.form.get('item-id')
        item_status = request.form.get('item-status')
        update_item_status(item_id, item_status)
        return redirect(url_for('index'))

    return app