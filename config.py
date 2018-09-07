import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASES_URI='postgresql+psycopg2://postgres:von@localhost/watchlist'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vonmutinda:von@localhost/minuteOne'


class ProdConfig():
    pass

class DevConfig():
    DEBUG = True

config_options = {
    'development' : DevConfig ,
    'production'  : ProdConfig
}