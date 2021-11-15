from flask import render_template
from flask.views import MethodView
from src.models import Services

class IndexController(MethodView):

    def get(self):
        return render_template('public/index.html')

class ServicesController(MethodView):
    
    def __init__(self) -> None:
        pass
    
    def get(self):
        services: Services = Services.query.all()
        return render_template('public/services.html', services=services)