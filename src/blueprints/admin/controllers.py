from flask import redirect, request, render_template, flash, url_for
from flask.views import MethodView
from src.hooks import verify_user
from src.models import Services, Appointment, User
from src.database import db

class PanelController(MethodView):
    
    decorators = [verify_user(verify_role=True)]
    
    def __init__(self) -> None:
        pass
    
    def get(self):
        appointments: Appointment = Appointment.query.all()
        return render_template('private/admin/panel.html', appointments=appointments)
    
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

class PanelUsersController(MethodView):
    
    def get(self):
        users: User = User.query.all()
        return render_template('private/admin/users.html', users=users)
    
    def post(self):
        rol = request.form['rol']
        uid = request.form['uid']
        print(rol, uid)
        try:
            user: User = User.query.filter_by(uid=uid).first()
            if user.is_admin:
                user.is_admin = False
                db.session.commit()
                flash('Se ha actualizado el rol del usuario', 'success')
                return redirect(url_for('admin.panel'))
            user.is_admin = True
            db.session.commit()
            flash('Se ha actualizado el rol del usuario', 'success')
        except Exception:
            flash('Ha ocurrido un error', 'error')
        return redirect(url_for('admin.panel'))

class AppointmentsDeleteController(MethodView):
    
    decorators = [verify_user(verify_role=True)]
    
    def get(self, uid):
        appointment: Appointment = Appointment.query.filter_by(uid=uid).first()
        db.session.delete(appointment)
        db.session.commit()
        flash('Se ha cancelado la cita', 'success')
        return redirect(url_for('admin.panel'))