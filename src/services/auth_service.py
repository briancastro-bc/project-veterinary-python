from flask import flash, redirect, session
from flask.helpers import url_for
from werkzeug.security import check_password_hash, generate_password_hash
from src.models import User
from src.database import db

class AuthService:

    def signup(self, name, last_name, email, password):
        user: User = User.query.filter_by(email=email).first()
        if not user:
            hash_password = generate_password_hash(password)
            try:
                new_user: User = User(email, hash_password, name, last_name)
                db.session.add(new_user)
                db.session.commit()
                flash('Te haz registrado, inicia sesion', 'success')
                return redirect(url_for('auth.login'))
            except Exception:
                flash('Ocurrio un error mientras intentabamos registrarte, reintenta', 'warning')
                return redirect(url_for('auth.signup'))
        flash('El email ya se encuentra registrado', 'warning')
        return redirect(url_for('auth.signup'))

    def login(self, email, password):
        user: User = User.query.filter_by(email=email).first()
        if user:
            verify_password = check_password_hash(user.password, password)
            if verify_password:
                session['user'] = user.email
                session['username'] = user.name
                session['user_uid'] = user.uid
                session['user_role'] = user.is_admin
                flash(f'Hola {user.name}! Haz iniciado sesion', 'success')
                return redirect(url_for('index'))
            flash('Credenciales de acceso incorrectas', 'warning')
            return redirect(url_for('auth.login'))
        flash('Credenciales de acceso incorrectas', 'warning')
        return redirect(url_for('auth.login'))
    
    def logout(self):
        session.clear()
        return redirect(url_for('auth.login'))