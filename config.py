import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  
    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class DevConfig():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutinda:von12@localhost/otouch'
    DEBUG = True

config_options = {
    'development' : DevConfig ,
    'production'  : ProdConfig
}