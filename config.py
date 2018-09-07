import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI='sqlite:///C:\\Users\\Username\\AppData\\Roaming\\Appname\\mydatabase.db'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2:///' + os.path.join(basedir, 'minuteone.db')

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vonmutinda:von@localhost/minuteone'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig():
    pass

class DevConfig():
    DEBUG = True

config_options = {
    'development' : DevConfig ,
    'production'  : ProdConfig
}