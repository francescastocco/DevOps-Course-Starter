import os
from flask_login import UserMixin

from todo_app.data.classes.user_roles import UserRoles


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.role = UserRoles.WRITER if id == os.getenv('ADMIN_USER_ID') else UserRoles.READER
        self.has_write_access = self.role == UserRoles.WRITER