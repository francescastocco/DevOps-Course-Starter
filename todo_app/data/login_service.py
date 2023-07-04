import flask_login
from todo_app.data.classes.user import User


def login_user(github_user):
        github_user_id = github_user['id']
        flask_login.login_user(User(github_user_id))