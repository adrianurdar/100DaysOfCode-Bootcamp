from functools import wraps
from flask_login import current_user
from flask import render_template, abort


# ONLY ADMIN DECORATOR
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return render_template(abort(403))
        return f(*args, **kwargs)
    return decorated_function
