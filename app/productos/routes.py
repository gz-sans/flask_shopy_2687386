from flask import render_template, redirect, flash
from app.productos import productos
import app
import os
from .forms import NewProductForm,editProductForm


@productos.route('/create',methods= ['GET', 'POST'])
def crear():
    #Guardar el producto en base de datos
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #Subir imagen la carpeta images
        #campo de imagen(filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd()+"/app/productos/images/"+ p.imagen))
        flash("Producto registrado correctamente")
        return redirect('/productos/list')
    return render_template('new.html', 
                            form = form)

@productos.route('/list')
def listar():
    #seleccionar prodcutos
    productos =app.models.Producto.query.all()
    return render_template("list.html",
                            productos = productos)


@productos.route('/update/<producto_id>',
                methods=['GET','POST'])

def actualizar(producto_id):
    p=app.models.Producto.query.get(producto_id)
    form = editProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Producto actualizado correctamente")
        return redirect('/productos/list')
    return render_template('new.html',
                            form=form)


@productos.route('/delete/<producto_id>')
    
def eliminar(producto_id):
    p=app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("producto eliminado corretamente")
    return redirect('/productos/list')