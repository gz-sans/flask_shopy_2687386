from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    Username =StringField(label='nombre de usuario',
                        validators=[InputRequired(
                        message="username requerido"
                        )])
    password =PasswordField(label='clave')
    submit =SubmitField(label='iniciar sesion',
                        validators=[InputRequired(
                        message="contraseña requerida"
                        )])
