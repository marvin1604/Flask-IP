from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#se crea la clase para usar Flask_wtf
class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    submit =SubmitField("Enviar")

class TodoForm(FlaskForm):
    description = StringField("Descripcion", validators = [DataRequired()])
    submit = SubmitField("Crear")




