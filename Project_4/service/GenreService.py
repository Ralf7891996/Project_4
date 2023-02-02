from dao import GenreDAO
from dao.model.genre import Genre


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self, page):
        return self.dao.get_all(page)

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def create(self, data):
        genre = Genre(**data)
        return self.dao.create(genre)

    def update(self, data):
        update_genre = self.get_one(data.get("id"))
        update_genre.name = data.get("name")
        return self.dao.update(update_genre)

    def update_part(self, data):
        update_genre = self.get_one(data.get("id"))
        if data.get("name") is not None:
            update_genre.name = data.get("name")
        return self.dao.update(update_genre)

    def delete(self, gid):
        return self.dao.delete(gid)