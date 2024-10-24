from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.Integer, default=time.time())
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    books = db.relationship('Book', backref='genre', lazy=True)
    