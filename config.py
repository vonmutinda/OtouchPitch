import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI='sqlite:///C:\\Users\\Username\\AppData\\Roaming\\Appname\\mydatabase.db'
    # SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
    #     'postgresql+psycopg2:///' + os.path.join(basedir, 'minuteone.db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:von@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig():
    DEBUG = True

config_options = {
    'development' : DevConfig ,
    'production'  : ProdConfig
}