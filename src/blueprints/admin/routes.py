from .controllers import PanelController, PanelServicesController

admin_routes: dict = {
    "panel": "/panel", "panel_controller": PanelController.as_view("panel"),
}

services_routes: dict = {
    "create": "/service/create", "create_controller": PanelServicesController.as_view("services_create")
}