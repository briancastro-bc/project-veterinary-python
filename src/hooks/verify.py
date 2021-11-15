from flask import session, url_for, redirect
from src.models import User
import functools

def verify_user(verify_role: bool=False):
    def _verify_user(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if session:
                if verify_role:
                    user: User = User.query.filter_by(email=session['user']).first()
                    if user.is_admin:
                        return f(*args, **kwargs)
                    return redirect('/404')
                return f(*args, **kwargs)
            return redirect(url_for('auth.login'))
        return wrapper
    return _verify_user