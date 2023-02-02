from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers.decorators import auth_required
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

# создаем CBV для обработки GET и POST запросов
@director_ns.route("/")
class DirectorsView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        all_directors = director_service.get_all(page)
        return directors_schema.dump(all_directors), 200

    @auth_required
    def post(self):
        req_json = request.json
        new_director = director_service.create(req_json)
        return "director_added", 201, {"location": f"/directors/{new_director.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    @auth_required
    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "director_update", 204

    @auth_required
    def patch(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update_part(req_json)
        return "director_update", 204

    @auth_required
    def delete(self, did):
        director_service.delete(did)
        return "director_deleted", 204
