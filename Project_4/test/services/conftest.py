import pytest
from unittest.mock import MagicMock

from dao.DirectorDAO import DirectorDAO
from dao.GenreDAO import GenreDAO
from dao.MovieDAO import MovieDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db


# Создаем фикстуру с моком для DirectorDAO
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    ralf = Director(id=1, name='ralf')
    cris = Director(id=2, name='cris')

    director_dao.get_all = MagicMock(return_value=[ralf, cris])
    director_dao.get_one = MagicMock(return_value=ralf)
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock(return_value=None)
    director_dao.update = MagicMock(return_value="update")
    return director_dao


# Создаем фикстуру с моком для GenreDAO
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    test_data_1 = Genre(id=1, name='test_1')
    test_data_2 = Genre(id=2, name='test_2')

    genre_dao.get_all = MagicMock(return_value=[test_data_1, test_data_2])
    genre_dao.get_one = MagicMock(return_value=test_data_1)
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


# Создаем фикстуру с моком для  MovieDAO
@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1,
                    title='movie_1',
                    description='description',
                    trailer='trailer',
                    year=2007,
                    rating=6.5,
                    genre_id=1,
                    genre=db.relationship("Genre"),
                    director_id=2,
                    director=db.relationship("Director")
                    )

    movie_2 = Movie(id=1,
                    title='movie_2',
                    description='description',
                    trailer='trailer',
                    year=2017,
                    rating=9.5,
                    genre_id=1,
                    genre=db.relationship("Genre"),
                    director_id=1,
                    director=db.relationship("Director")
                    )

    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.create = MagicMock(return_valye=Movie(id=3, year=2006))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock(return_value=None)
    movie_dao.partially_update = MagicMock()
    return movie_dao