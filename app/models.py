from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from . import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_code = db.Column(db.Integer, nullable=False, unique=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    weight = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    imagepath = db.Column(db.String(100))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    products = db.relationship("Product", backref="category", lazy=True)

    def __repr__(self):
        return self.name


db.create_all()
