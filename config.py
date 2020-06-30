import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Production(object):
    """
    Production environment configurations
    """
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:Ingreso871@localhost/Irso"
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    #JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'production': Production,
}
