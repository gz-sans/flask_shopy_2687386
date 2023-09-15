from flask_login import login_user, current_user, logout_user
from flask import render_template, redirect, flash 
from app.auth import auth
from .forms import LoginForm
import app

@auth.route('/login',
            methods=["GET",'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #selecciona al cliente por username
        c =app.models.Cliente.query.filter_by(username=form.Username.data).first()
        if c is None or not c.check_password(form.password.data):
            flash('usuario no existe')
            redirect('/auth/login')
            #mensaje flask de usuario no existente
        else:
            flash('Bienvenido al sistema')
            login_user(c, remember=True)
            return redirect('/clientes/list')
    return render_template('login.html', 
                            form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')