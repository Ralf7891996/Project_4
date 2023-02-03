
from dao.model.user import FavoriteMovie


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def added(self, data_movie):
        favorite_movie = FavoriteMovie(**data_movie)
        self.session.add(favorite_movie)
        self.session.commit()
        return favorite_movie

    def delete(self, delete_movie):
        delete_movie = FavoriteMovie(**delete_movie)
        self.session.delete(delete_movie)
        self.session.commit()