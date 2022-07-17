from . import db

from werkzeug.security import generate_password_hash

import datetime

class User(db.Model):
    __tablename__ = 'ships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(102), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
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
        user = User(username=username, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return user