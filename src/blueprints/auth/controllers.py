from flask import request, make_response, jsonify
from flask.views import MethodView

class LoginController(MethodView):

    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        return "Login controller works!"

class SignupController(MethodView):

    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        return "Signup controller works!"