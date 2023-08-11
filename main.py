#importacion o dependencias del proyecto
from flask import Flask
from config import Config
from flask_migrate import Migrate
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app , db )



# entidades del proyecto
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric( precision =10 , scale = 2))
    imagen = db.Column(db.String(120), unique = True)
    
class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True)
    feche = db.Column(db.Datetime , default = datetime.utcnow )