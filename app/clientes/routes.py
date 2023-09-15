from flask import render_template, redirect, flash
from app.clientes import Clientes
from flask_login import login_required
import app
import os
from .forms import NewClientForm, EditClientForm


@Clientes.route('/create',methods=['GET', 'POST'])
@login_required
def creat():
        #Guardar el producto en base de datos
    p = app.models.Cliente()
    form = NewClientForm()
    c=p
    if form.validate_on_submit():
        form.populate_obj(p)
        c.setPassword(form.password.data)
        print(c)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Cliente registrado correctamente")
        return redirect('/clientes/list')
    return render_template('create.html', 
                            form = form)

@Clientes.route('/list')
@login_required
def listar():
    #seleccionar prodcutos
    clientes =app.models.Cliente.query.all()
    return render_template("listar.html",
                            clientes = clientes)

@Clientes.route('/update/<cliente_id>', methods=['GET', 'POST'])
@login_required
def edit(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect('/clientes/list')
    return render_template('create.html', form=form)

@Clientes.route('/delete/<cliente_id>')
@login_required
def delete(cliente_id):
    p=app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("cliente eliminado corretamente")
    return redirect('/clientes/list')