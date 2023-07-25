import os
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required
import flask_login
from todo_app.data.classes.user import User
from todo_app.data.database_client import create_item, delete_item, get_all_items, update_item_status
from todo_app.data.decorators.user_role_decorator import requires_write_access
from todo_app.data.github_client import get_access_token, get_authenticated_github_user
from todo_app.data.login_service import login_user
from todo_app.flask_config import Config
from todo_app.view_models.items_view_model import ItemsViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = os.getenv('CLIENT_ID')
        return redirect(f'https://github.com/login/oauth/authorize?client_id={client_id}')

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        user = flask_login.current_user
        items = ItemsViewModel(get_all_items(), user)
        return render_template('index.html', view_model=items)
    
    @app.route('/login/callback')
    def auth():
        auth_code = request.args.get('code')
        access_token = get_access_token(auth_code)
        github_user = get_authenticated_github_user(access_token)
        login_user(github_user)
        return redirect(url_for('index'))
    
    @app.route('/create', methods = ['POST'])
    @login_required
    @requires_write_access
    def create():
        new_item_title = request.form.get('item-title')
        create_item(new_item_title)
        return redirect(url_for('index'))

    @app.route('/update', methods = ['POST'])
    @login_required
    @requires_write_access
    def update():
        item_id = request.form.get('item-id')
        item_status = request.form.get('item-status')
        update_item_status(item_id, item_status)
        return redirect(url_for('index'))
    
    @app.route('/delete', methods = ['POST'])
    @login_required
    @requires_write_access
    def delete():
        item_id = request.form.get('item-id')
        delete_item(item_id)
        return redirect(url_for('index'))

    return app