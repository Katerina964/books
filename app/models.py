from app import db
from datetime import datetime


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.DateTime())
    books = db.relationship('Book', backref='author',
                                lazy='dynamic')
    def __repr__(self):
        return self.name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return self.title
