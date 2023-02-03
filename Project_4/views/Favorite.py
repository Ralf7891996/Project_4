from flask import request
from flask_restx import Namespace, Resource


from helpers.decorators import auth_required
from implemented import favorite_service

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/<int:mid>')
class FavoriteViews(Resource):
    @auth_required
    def post(self, mid):
        data = request.headers['Authorization']
        favorite_service.added(mid, data)
        return "movie_added", 201

    @auth_required
    def delete(self, mid):
        data = request.headers['Authorization']
        favorite_service.delete(mid, data)
        return "user_delete", 204