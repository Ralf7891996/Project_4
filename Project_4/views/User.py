from flask import request
from flask_restx import Namespace, Resource

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return user_schema.dump(user), 200

    def patch(self, uid):
        user_data = request.json
        user_data['id'] = uid
        user_service.part_update(user_data)
        return "user_update", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "user_delete", 204

@user_ns.route('/password/<int:uid>')
class UserView(Resource):
    def put(self, uid):
        user_data = request.json
        user_data['id'] = uid
        user_service.update(user_data)
        return "user_update", 204

