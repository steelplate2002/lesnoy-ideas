# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    home_number = db.Column(db.Integer)
    phone_number = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role',
        backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    name = db.Column(db.String(100))
    level = db.Column(db.Integer)