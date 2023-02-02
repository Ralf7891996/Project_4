from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        data_request = request.json
        email = data_request.get("email", None)
        password = data_request.get("password", None)
        if None in [email, password]:
            return 400
        new_user = auth_service.create(data_request)
        return "user_registered", 201 # {"location": f"/users/{new_user.id}"}


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        data_request = request.json
        email = data_request.get("email", None)
        password = data_request.get("password", None)
        if not auth_service.check_register(email, password):
            return 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        data_request = request.json
        token = data_request.get('refresh_token')
        if token is None:
            return 400
        tokens = auth_service.aprove_refresh_token(token)
        return tokens, 201