from flask_sqlalchemy import SQLAlchemy

from . import app

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    imagepath = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    products = db.relationship('Product', backref='category', lazy=True)
    def __repr__(self):
        return self.name


db.create_all()
