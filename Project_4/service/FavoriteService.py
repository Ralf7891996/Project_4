import jwt

from dao import FavoriteDAO
from helpers.constant import SECRET, ALGO
from service import UserService


class FavoriteService:
    def __init__(self, dao: FavoriteDAO, user_service: UserService):
        self.dao = dao
        self.user_service = user_service

    def added(self, mid, data):
        token = data.split("Bearer ")[-1]
        data_user = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
        email = data_user.get('email')
        user = self.user_service.get_by_email(email)
        favorite_movie = {
            "user_id": user.id,
            "movie_id": mid
        }
        return self.dao.added(favorite_movie)

    def delete(self, mid, data):
        token = data.split("Bearer ")[-1]
        data_user = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
        email = data_user.get('email')
        user = self.user_service.get_by_email(email)
        delete_movie = {
            "user_id": user.id,
            "movie_id": mid
        }
        return self.dao.delete(delete_movie)