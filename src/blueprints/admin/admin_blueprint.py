from flask import Blueprint 
from .routes import admin_routes, services_routes, appointments_routes

class AdminBlueprint:
    
    admin: Blueprint
    
    @classmethod
    def init_blueprint(cls):
        cls.admin = Blueprint('admin', __name__, url_prefix='/admin')
        cls.__register_routes()
        return cls.admin
    
    @classmethod
    def __register_routes(cls):
        cls.admin.add_url_rule(admin_routes['panel'], view_func=admin_routes['panel_controller'])
        cls.admin.add_url_rule(services_routes['create'], view_func=services_routes['create_controller'])
        cls.admin.add_url_rule(appointments_routes['delete'], view_func=appointments_routes['delete_controller'])
        cls.admin.add_url_rule(admin_routes['users'], view_func=admin_routes['users_controller'])