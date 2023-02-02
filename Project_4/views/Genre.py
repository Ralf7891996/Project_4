from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from helpers.decorators import auth_required
from implemented import genre_service

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


# создаем CBV для обработки GET и POST запросов
@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        all_genres = genre_service.get_all(page)
        return genres_schema.dump(all_genres)

    @auth_required
    def post(self):
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return "genre_added", 201, {"location": f"/genres/{new_genre.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre)

    @auth_required
    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "genre_update", 204

    @auth_required
    def patch(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update_part(req_json)
        return "genre_update", 204

    @auth_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "genre_deleted", 204