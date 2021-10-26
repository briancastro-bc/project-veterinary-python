from .controllers import LoginController, SignupController

auth_routes = {
    "login": "/login", "login_controller": LoginController.as_view("login"),
    "signup": "/signup", "signup_controller": SignupController.as_view("signup")
}