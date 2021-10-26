from src.controllers import IndexController, NotFoundController

root_routes = {
    "index": "/", "index_controller": IndexController.as_view('index')
}

error_routes = {
    "not_found": 404, "not_found_controller": NotFoundController.as_view('not_found')
}