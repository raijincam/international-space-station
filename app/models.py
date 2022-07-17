from turtle import back, backward
from . import db, ma

from werkzeug.security import generate_password_hash

import datetime

class Ship(db.Model):
    __tablename__ = 'ship'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.String(102), nullable=False)
    vigency = db.Column(db.String(100), unique=True, nullable=False)
    kind = db.Column(db.String(50), unique=True, nullable=False)
    combustible = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)

    def __str__(self):
        return self.username
    
    @classmethod
    def create_user(cls, username, password, email):
        ship = Ship(username=username, password=password, email=email)

        db.session.add(ship)
        db.session.commit()

        return ship

class type_ship(db.Model):
    __tablename__ = 'type_ship'

    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String(255), nullable=False)
    #ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'), nullable=False)

class type_ship_schema:
    class meta:
        model = type_ship
        sqla_session = db.session
    

class combustibles(db.Model):
    __tablename__ = 'combustibles'

    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String(255), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('ship.id'), nullable=False)

class combustibles_schema:
    class meta:
        model = combustibles
        sqla_session = db.session

class country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String(255), nullable=False)


class country_schema:
    class meta:
        model = country
        sqla_session = db.session