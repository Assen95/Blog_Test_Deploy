from functools import wraps
from flask import abort
from flask_login import current_user

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        else:
            abort(403)  # Forbidden access
    return decorated_function
