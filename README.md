# flask_shopy_2687386
comandos:

1. pip install -r requirements.txt

2. flask db init

3. flask  db migrate  

4.flask db upgrade 

5. flask --app main --debug run

base de datos:
create database flask_shopy_2687386;
use flask_shopy_2687386;


from app import db
from app import Cliente

Crea un espacio para interactuar con la aplicación

app.app_context().push()

Crea un nuevo cliente y establece la contraseña utilizando el método setPassword

nuevo_cliente = Cliente(username="gz sans omega", email="gzsans@gmail")
nuevo_cliente.setPassword("1234")

Agrega el cliente a la base de datos

db.session.add(nuevo_cliente)
db.session.commit()

dependecias faltantes:
1- pip install Flask-Login
2- pip install flask-bootstrap 
