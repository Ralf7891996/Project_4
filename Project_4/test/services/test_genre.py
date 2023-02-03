import pytest

from service.GenreService import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        return GenreService(genre_dao)

    def test_get_all(self, genre_service, page=None):
        genres = genre_service.get_all(page)
        assert len(genres) > 0

    def test_get_one(self, genre_service):
        genre = genre_service.get_one(1)
        assert genre.name is not None
        assert genre.id is not None

    def test_create(self, genre_service):
        data_g = {'name': 'test'}
        genre = genre_service.create(data_g)
        assert genre.id is not None

    def test_update(self, genre_service):
        data_g = {'name': 'test'}
        genre_service.update(data_g)

    def test_delete(self, genre_service):
        genre_service.delete(1)
