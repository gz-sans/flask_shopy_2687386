from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ClientForm():
    username = StringField("ingrese su usuario",
                           validators=[InputRequired(
                               message="usuario requerido"
                           )])
    password = StringField("ingrese su contraseña",
                           validators=[InputRequired(
                               message="contraseña requerido"
                           )])
    email = StringField("ingrese su email",
                           validators=[InputRequired(
                               message="rmail requerido"
                           )])
    
class NewClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Actualizar")