from flask import request, render_template, session
from flask.helpers import flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect
from src.hooks import verify_user
from src.database import db
from src.models import Pet, Services, Appointment

class AppointmentsController(MethodView):
    
    decorators = [verify_user()]
    
    def get(self):
        pets: Pet = Pet.query.filter_by(owner=session['user_uid']).first()
        services: Services = Services.query.all()
        return render_template('private/appointment.html', pets=pets, services=services)
    
    def post(self):
        pet = request.form['pet']
        service = request.form['service']
        to_day = request.form['to_day']
        try:
            new_appointment = Appointment(service, pet, to_day)
            db.session.add(new_appointment)
            db.session.commit()
            flash('Hemos registrado tu cita para la fecha indicada', 'success')
        except Exception:
            flash('Ocurrio un error al sacar la cita', 'error')
        return redirect(url_for('index'))