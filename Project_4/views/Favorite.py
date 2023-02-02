
from flask_restx import Namespace, Resource

from dao.model.user import FavoriteMovieSchema
from helpers.decorators import auth_required
from implemented import favorite_service

favorite_ns = Namespace('favorite')
favorite_schema = FavoriteMovieSchema(many=True)


@favorite_ns.route('/')
class FavoriteView(Resource):
    def get(self):
        favorite_movies = favorite_service.get_all()
        return favorite_schema.dump(favorite_movies), 200


@favorite_ns.route('/<int:uid>')
class FavoriteView(Resource):
    def get(self, uid):
        favorite_movies = favorite_service.get_by_user(uid)
        return favorite_schema.dump(favorite_movies), 200


@favorite_ns.route('/movies/<int:mid>')
class FavoriteViews(Resource):
    @auth_required
    def post(self, mid):
        movie_add = favorite_service.added(mid)
        return "movie_added", 201, {"location": f"/favorite/movies/<int::mid>/{movie_add.id}"}

    @auth_required
    def delete(self, mid):
        favorite_service.delete(mid)
        return "user_delete", 204