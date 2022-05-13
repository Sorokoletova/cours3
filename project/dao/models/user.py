from project.setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    favorite_genre = db.Column(db.String)
