from flask import Blueprint
from .routes import auth_routes

class AuthBlueprint:

    auth: Blueprint

    @classmethod
    def init_blueprint(cls):
        cls.auth = Blueprint('auth', __name__, url_prefix='/auth')
        cls.__register_routes()
        return cls.auth
    
    @classmethod
    def __register_routes(cls):
        cls.auth.add_url_rule(auth_routes['login'], view_func=auth_routes['login_controller'], methods=['GET', 'POST'])
        cls.auth.add_url_rule(auth_routes['signup'], view_func=auth_routes['signup_controller'], methods=['GET', 'POST'])