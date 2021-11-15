from .controllers import LoginController, SignupController, LogoutController

auth_routes = {
    "login": "/login", "login_controller": LoginController.as_view("login"),
    "signup": "/signup", "signup_controller": SignupController.as_view("signup"),
    "logout": "/logout", "logout_controller": LogoutController.as_view("logout")
}