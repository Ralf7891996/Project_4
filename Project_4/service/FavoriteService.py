from dao import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_all(self):
        return self.get_all()

    def get_by_user(self, uid):
        return self.dao.get_by_user(uid)

    def added(self, mid):
        movie = self.dao.get_by_movie(mid)
        return self.dao.added(movie)

    def delete(self, mid):
        return self.dao.delete(mid)