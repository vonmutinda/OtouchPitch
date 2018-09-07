from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# **** instantiate extensions ****
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # *** app configurations *** #
    app.config.from_object(config_options[config_name])


    # *** Init app extensions *** #
    bootstrap.init_app(app)

     # *** Registering the blueprint ***
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app