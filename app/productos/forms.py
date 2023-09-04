from flask_wtf import  FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese nombre del producto:", 
                        validators = [InputRequired(
                            message='nombre requerido'
                        )])
    precio = IntegerField("Ingrese precio del producto:", 
                        validators = [
                            InputRequired(
                                message='producto requerido'
                        ),
                            NumberRange(
                                message="precio fuera de rango",
                                min = 10000,
                                max = 100000
                            )
                        ])
    imagen = FileField( label="imgen del producto",
                        validators=[
                            FileRequired(
                                message="imagen requerida"),
                            FileAllowed(["jpg","png"] , 
                                        message="solo se aceptan archivo png y jpg")
                        ])
    submit = SubmitField("Guardar")