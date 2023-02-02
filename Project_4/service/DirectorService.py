from dao import DirectorDAO
from dao.model.director import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self, page):
        return self.dao.get_all(page)

    def get_one(self, did):
        return self.dao.get_one(did)

    def create(self, data):
        director = Director(**data)
        return self.dao.create(director)

    def update(self, data):
        update_director = self.get_one(data.get("id"))
        update_director.name = data.get("name")
        return self.dao.update(update_director)

    def update_part(self, data):
        update_director = self.get_one(data.get("id"))
        if data.get("name") is not None:
            update_director.name = data.get("name")
        return self.dao.update(update_director)

    def delete(self, did):
        return self.dao.delete(did)