# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.Auth import auth_ns
from views.Director import director_ns
from views.Favorite import favorite_ns
from views.Genre import genre_ns
from views.Movie import movie_ns
from views.User import user_ns


def create_app(config_object: Config):
    """
    Функция создает приложение, на вход принимает конфигурацию
    """
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application: Flask):
    """
    Функция создает Api и добавляет неймспейсы
    """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorite_ns)
    api.add_namespace(auth_ns)
    data_create(application, db)


def data_create(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())

if __name__ == '__main__':
    app.run(port=8000, debug=True)
