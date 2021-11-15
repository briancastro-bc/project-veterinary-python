from flask import Flask
from os import getenv
from src.blueprints import AuthBlueprint,  AdminBlueprint
from src.routes.root_routes import root_routes, error_routes, pets_routes
from src.database import db

class Application:

    app: Flask

    @classmethod
    def init_app(cls) -> Flask:
        cls.app = Flask(__name__)
        cls.__settings()
        db.init_app(cls.app)
        db.create_all(app=cls.app)
        return cls.app
    
    @classmethod
    def __settings(cls) -> None:
        try:
            cls.app.config.from_mapping(
                SECRET_KEY=getenv('SECRET_KEY')
            )
            cls.app.config.from_pyfile('../appconfig.cfg')
            cls.app.config['SQLALCHEMY_DATABASE_URI'] = cls.app.config['DATABASE_CONN']
            cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            cls.__register_blueprints()
            cls.__register_root_routes()
        except KeyError as ke:
            raise ke
        except Exception as e:
            raise e
    
    @classmethod
    def __register_blueprints(cls) -> None:
        cls.app.register_blueprint(AuthBlueprint.init_blueprint())
        cls.app.register_blueprint(AdminBlueprint.init_blueprint())
    
    @classmethod
    def __register_root_routes(cls) -> None:
        cls.app.add_url_rule(root_routes['index'], view_func=root_routes['index_controller'], endpoint='index')
        cls.app.add_url_rule(pets_routes['create'], view_func=pets_routes['create_controller'], methods=['POST'])
        cls.app.add_url_rule(root_routes['services'], view_func=root_routes['services_controller'], methods=['GET'])
        cls.__register_error_handlers()
    
    @classmethod
    def __register_error_handlers(cls) -> None:
        cls.app.register_error_handler(error_routes['not_found'], error_routes['not_found_controller'])