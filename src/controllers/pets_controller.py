from flask import request, redirect, session
from flask.helpers import flash, url_for
from flask.views import MethodView
from src.models import Pet
from src.database import db

class PetsController(MethodView):
    
    def post(self):
        name: str = request.form['name']
        breed: str = request.form['breed']
        age: int = request.form['age']
        owner: str = session['user_uid']
        try:
            new_pet: Pet = Pet(name, breed, age, owner)
            db.session.add(new_pet)
            db.session.commit()
            flash('Hemos registrado tu mascota', 'success')
        except Exception:
            flash('Ocurrio un error mientras registrabamos tu mascota')
        return redirect(url_for('index'))