from . import db

from flask_login import UserMixin

from sqlalchemy.sql import func

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)

    email = db.Column(db.String(150), unique = True)

    password = db.Column(db.String(150))

    first_name = db.Column(db.String(150))

    # last_name = db.Column(db.String(150))

class Contact(db.Model):

    srl = db.Column(db.Integer, primary_key = True)

    message = db.Column(db.String(200))

    name = db.Column(db.String(150))

    email = db.Column(db.String(150))

    subject = db.Column(db.String(150))

class Add_Product(db.Model):

    idd = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(200))

    price = db.Column(db.String(20))



