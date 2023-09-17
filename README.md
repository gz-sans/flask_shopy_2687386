# Proyecto de Prueba Python - Flask_Shopy_2687386

Este es un proyecto de prueba en Python donde se están explorando las prácticas comunes para el desarrollo de aplicaciones con Flask. El proyecto ya ha logrado implementar un sistema de inicio de sesión, la creación de clientes y productos, y la encriptación de contraseñas para los clientes.


1. Instala las dependencias necesarias ejecutando el siguiente comando:
   pip install -r requirements.txt
2. Inicializa la base de datos con los siguientes comandos:
   flask db init
   flask db migrate
   flask db upgrade
3. Crea una base de datos en tu sistema de gestión de bases de datos (por ejemplo, MySQL) con el nombre flask_shopy_2687386.
4. Para crear un usuario de prueba, abre una terminal Python y ejecuta los siguientes comandos:
   from app import db, Cliente
   from app import app
   app.app_context().push()
   nuevo_cliente = Cliente(username="gz sans omega", email="gzsans@gmail.com")
   nuevo_cliente.setPassword("1234")
   db.session.add(nuevo_cliente)
   db.session.commit()

   



