from flask import Flask, render_template
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import Clientes
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#regitrar modulos(bluePrints)

#registres blueprint de productos
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#registres blueprint de clientes
app.register_blueprint(Clientes)

from .models import Cliente,Venta,Producto,Detalle

@app.route('/prueba')
def prueba():
    return render_template("base.html")