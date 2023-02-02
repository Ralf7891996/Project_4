from dao.model.movie import Movie
from dao.model.user import FavoriteMovie


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(FavoriteMovie).all()

    def get_by_user(self, uid):
        return self.session.query(FavoriteMovie).get(uid)

    def get_by_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def added(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        delete_movie = self.get_by_movie(mid)
        self.session.delete(delete_movie)
        self.session.commit()