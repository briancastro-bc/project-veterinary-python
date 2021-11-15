from flask import redirect, request, render_template, flash, url_for
from flask.views import MethodView
from src.hooks import verify_user
from src.models import Services
from src.database import db

class PanelController(MethodView):
    
    decorators = [verify_user(verify_role=True)]
    
    def __init__(self) -> None:
        pass
    
    def get(self):
        return render_template('private/admin/panel.html')
    
    def post(self):
        pass

class PanelServicesController(MethodView):
    
    decorators = [verify_user(verify_role=True)]
    
    def get(self):
        pass
    
    def post(self):
        name: str = request.form['name']
        image: str = request.form['image']
        description: str = request.form['description']
        value: float = request.form['value']
        try:
            new_service: Services = Services(name, image, description, value)
            db.session.add(new_service)
            db.session.commit()
            flash('Se creado un nuevo servicio', 'success')
        except Exception:
            flash('Ocurrio un error mientras creabamos el servicio')
        return redirect(url_for('admin.panel'))
    
    def put(self):
        pass
    
    def delete(self):
        pass