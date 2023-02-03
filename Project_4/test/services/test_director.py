import pytest

from service.DirectorService import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        return DirectorService(director_dao)

    def test_get_all(self, director_service):
        directors = director_service.get_all()
        assert len(directors) > 0

    def test_get_one(self, director_service):
        director = director_service.get_one(1)
        assert director.name is not None
        assert director.id is not None

    def test_create(self, director_service):
        director_data = {"name": "Step"}
        director = director_service.create(director_data)
        assert director.id is not None

    def test_update(self, director_service):
        director_data = {"name": "Step"}
        director = director_service.update(director_data)
        assert director is not None

    def test_delete(self, director_service):
        director = director_service.delete(3)
        assert director is None
