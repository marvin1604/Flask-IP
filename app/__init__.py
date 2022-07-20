from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    #creamos una llave secreta y no guardaremos la ip en cookie sino en sesion
    app.config.from_object(Config)
    
    return app