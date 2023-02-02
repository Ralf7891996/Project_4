from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()


class FavoriteMovie(db.Model):
    __tablename__ = 'favorite'
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    movie = db.relationship("Movie")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")


class FavoriteMovieSchema(Schema):
    movie_id = fields.Integer()
    user_id = fields.Integer()






