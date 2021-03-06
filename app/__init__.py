from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE


from config import config_options , Config

# **** instantiate extensions ****
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
simple = SimpleMDE()

photos = UploadSet("photos",IMAGES)


def create_app(config_name):
    app = Flask(__name__)

    # *** app configurations *** #
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    # *** Init app extensions *** #
    configure_uploads(app,photos)
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