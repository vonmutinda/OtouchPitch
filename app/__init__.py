from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE

from config import config_options

# **** instantiate extensions ****
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
simple = SimpleMDE()


def create_app(config_name):
    app = Flask(__name__)

    # *** app configurations *** #
    app.config.from_object(config_options[config_name])


    # *** Init app extensions *** #
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

     # *** Registering the blueprint ***
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate') 

    app.config['SECRET_KEY'] =  'bxxfcxa43xf7xd9xc6xefxf8c'


    return app