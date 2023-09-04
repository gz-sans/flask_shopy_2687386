from flask import render_template
from app.productos import productos
import app
import os
from .forms import NewProductForm


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
        return "imagen guardada"
    return render_template('new.html', 
                            form = form)

@productos.route('/delete')
def eliminar():
    return 'aqui vamos a eliminar productos'

@productos.route('/update')
def actualizar():
    return 'aqui vamos a actualizar los datos de los productos'