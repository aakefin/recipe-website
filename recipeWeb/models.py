from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500))
    ingredients = db.Column(db.JSON, nullable=False) 
    instructions = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return f'<Recipe {self.title}>'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(150))
    recipes = db.relationship('Recipe')