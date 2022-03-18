class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1111@localhost/blog'
    SECRET_KEY = '1111'
    SECURITY_PASSWORD_SALT = 'vrsjbdtijdsb'
    SECURITY_PASSWORD_HASH = 'bcrypt'
