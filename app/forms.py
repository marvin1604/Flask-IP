from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#se crea la clase para usar Flask_wtf
class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators= [DataRequired()])
    password = PasswordField("Contraseña", validators= [DataRequired()])
    submit =SubmitField("Iniciar Sesión")

class TodoForm(FlaskForm):
    description = StringField("Descripción", validators = [DataRequired()])
    submit = SubmitField("Crear")

class DeleteTodoForm(FlaskForm):
    submit = SubmitField("Borrar")

class UpdateTodoForm(FlaskForm):
    submit = SubmitField("Actualizar")






