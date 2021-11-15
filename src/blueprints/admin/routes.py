from .controllers import PanelController, PanelServicesController, AppointmentsDeleteController, PanelUsersController

admin_routes: dict = {
    "panel": "/panel", "panel_controller": PanelController.as_view("panel"),
    "users": "/users", "users_controller": PanelUsersController.as_view("users")
}

appointments_routes = {
    "delete": "/appointments/delete/<uid>", "delete_controller": AppointmentsDeleteController.as_view("appointments_delete")
}

services_routes: dict = {
    "create": "/service/create", "create_controller": PanelServicesController.as_view("services_create")
}