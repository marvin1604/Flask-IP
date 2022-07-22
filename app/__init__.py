from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    #creamos una llave secreta y no guardaremos la ip en cookie sino en sesion
    app.config.from_object(Config)

    #inicializamos la aplicacion con login manager
    login_manager.init_app(app)

    #registramos el nuevo blueprint
    app.register_blueprint(auth)


    return app