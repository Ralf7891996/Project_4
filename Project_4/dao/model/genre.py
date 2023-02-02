from setup_db import db
from marshmallow import Schema, fields

# модель Genre
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# схема Genre
class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
