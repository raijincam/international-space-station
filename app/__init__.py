from flask import Flask
from flask_bootstrap import Bootstrap
#from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
bootstrap = Bootstrap()
#csrf = CSRFProtect()

from .views import page
from .models import Ship

def create_app(environment):
    app.config.from_object(environment)

    #csrf.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(page)

    with app.app_context():

        db.init_app(app)
        db.create_all()

    return app