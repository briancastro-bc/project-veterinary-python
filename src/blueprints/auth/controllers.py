from flask import request, redirect, flash, session, render_template
from flask.views import MethodView
from src.services import AuthService

class LoginController(MethodView):

    def __init__(self) -> None:
        self.auth_service = AuthService()
    
    def get(self):
        return render_template('public/login.html')
    
    def post(self):
        email: str = request.form['email']
        password: str = request.form['password']
        return self.auth_service.login(email, password)

class SignupController(MethodView):

    def __init__(self) -> None:
        self.auth_service = AuthService()
    
    def get(self):
        return render_template('public/signup.html')
    
    def post(self):
        name: str = request.form['name']
        last_name: str = request.form['last_name']
        email: str = request.form['email']
        password: str = request.form['password']
        return self.auth_service.signup(name, last_name, email, password)

class LogoutController(MethodView):
    
    def __init__(self) -> None:
        self.auth_service = AuthService()
    
    def get(self):
        return self.auth_service.logout()