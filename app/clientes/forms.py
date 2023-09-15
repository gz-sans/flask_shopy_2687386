from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class ClientForm():
    username = StringField("ingrese su usuario",
                            validators=[InputRequired(
                                message="usuario requerido"
                            ), 
                            Length(1,120)])
    password = StringField("ingrese su contraseña",
                            validators=[InputRequired(
                                message="contraseña requerido"
                            ) , 
                            Length(10,10)])
    email = StringField("ingrese su email",
                            validators=[InputRequired(
                                message="email requerido"
                        ),
                                        Email(
                                message="debe tenea un @ y una direccion"
                        )])
    
class NewClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Actualizar")