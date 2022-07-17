
class Config:
    # SECRET_KEY = 'llavesecreta'
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:b3g1Nn3r.in.Fl4Sk202(1).@localhost/ships'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
    }
