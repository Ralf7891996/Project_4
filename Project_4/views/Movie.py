from flask import request
from flask_restx import Resource, Namespace, fields

from dao.model.movie import MovieSchema
from helpers.decorators import auth_required
from implemented import movie_service

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

resource_fields = movie_ns.model('Resource', {
    'title': fields.String,
    'description': fields.String,
    'trailer': fields.String,
    'year': fields.Integer,
    'rating': fields.Float,
    'genre_id': fields.Integer,
    'director_id': fields.Integer
})
# создаем CBV для обработки GET и POST запросов
@movie_ns.route('/')
class MoviesView(Resource):
    @movie_ns.marshal_with(resource_fields, as_list=True)
    @auth_required
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        status = request.args.get("status")
        page = request.args.get("page")
        filter = {
            "director_id": director_id,
            "genre_id": genre_id,
            "year": year,
            "status": status,
            "page": page}
        all_movies = movie_service.get_all(filter)
        return movies_schema.dump(all_movies), 200

    @movie_ns.marshal_with(resource_fields, 201)
    @auth_required
    def post(self):
        data = request.json
        new_movie = movie_service.create(data)
        return "movie_added", 201, {"location": f"/movies/{new_movie.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    @movie_ns.marshal_with(resource_fields, as_list=True)
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)

    @movie_ns.marshal_with(resource_fields, 204)
    @auth_required
    def put(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "movie_update", 204

    @auth_required
    def patch(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update_part(data)
        return "movie_update", 204

    @auth_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "movie_deleted", 204
