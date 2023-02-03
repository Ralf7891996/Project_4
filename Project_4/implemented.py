# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.DirectorDAO import DirectorDAO
from dao.FavoriteDAO import FavoriteDAO
from dao.GenreDAO import GenreDAO
from dao.MovieDAO import MovieDAO
from dao.UserDAO import UserDAO
from service.AuthService import AuthService
from service.DirectorService import DirectorService
from service.FavoriteService import FavoriteService
from service.GenreService import GenreService
from service.MovieService import MovieService
from service.UserService import UserService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(dao=user_dao)

favorite_dao = FavoriteDAO(db.session)
favorite_service = FavoriteService(favorite_dao, user_service)

auth_service = AuthService(user_service)


