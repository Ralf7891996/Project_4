import pytest

from service.MovieService import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        return MovieService(movie_dao)

    def test_get_all(self, movie_service):
        movies = movie_service.get_all(data_req={"page": None, "status": None})
        assert len(movies) > 0

    def test_get_one(self, movie_service):
        movie = movie_service.get_one(1)
        assert movie.id is not None
        assert movie.title is not None

    def test_create(self, movie_service):
        data_m = {'title': 'movie',
                  'description': 'description',
                  'trailer': 'trailer',
                  'year': 2006,
                  'rating': 8,
                  'genre_id': 1,
                  'director_id': 1}

        movie = movie_service.create(data_m)
        assert movie.id is not None

    def test_update(self, movie_service):
        data_m = {'title': 'movie',
                  'description': 'description',
                  'trailer': 'trailer',
                  'year': 2006,
                  'rating': 8,
                  'genre_id': 1,
                  'director_id': 1}

        movie_service.create(data_m)

    def test_delete(self, movie_service):
        movie = movie_service.delete(3)
        assert movie is None

    def test_partially_update(self, movie_service):
        data_m = {'title': 'movie_1',
                  'description': 'description',
                  'trailer': 'trailer'}
        movie_service.create(data_m)
