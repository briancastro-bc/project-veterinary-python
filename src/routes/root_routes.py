from src.controllers import IndexController, NotFoundController, PetsController, ServicesController, AppointmentsController

root_routes = {
    "index": "/", "index_controller": IndexController.as_view('index'),
    "services": "/services", "services_controller": ServicesController.as_view("services"),
    "appointments": "/appointments", "appointments_controller": AppointmentsController.as_view("appointments")
}

pets_routes = {
    "create": "/pet/create", "create_controller": PetsController.as_view('pets_create')
}

error_routes = {
    "not_found": 404, "not_found_controller": NotFoundController.as_view('not_found')
}