from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    #creamos una llave secreta y no guardaremos la ip en cookie sino en sesion
    app.config.from_object(Config)

    #registramos el nuevo blueprint
    app.register_blueprint(auth)

    return app