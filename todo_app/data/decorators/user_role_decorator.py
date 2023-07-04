from functools import wraps
from flask import abort

import flask_login


def requires_write_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not flask_login.current_user.has_write_access():
            abort(403)
        return f(*args, **kwargs)
    return decorated_function