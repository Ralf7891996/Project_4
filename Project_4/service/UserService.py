from flask import abort

from dao.UserDAO import UserDAO
from dao.model.user import User
import base64
import hashlib
import hmac

from helpers.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        user = self.dao.get_by_email(email)
        return user

    def create(self, user_data):
        user_data["password"] = self.get_hash(user_data["password"])
        user = User(**user_data)
        return self.dao.create(user)

    def update(self, user_data):
        user_update = self.get_one(user_data.get('id'))
        password_1 = user_data.get('password_1')
        password_2 = user_data.get('password_2')
        if None in [password_1, password_2]:
            abort(400)
        if not self.comprare_passwords(user_update.password, password_1):
            abort(400)
        user_update.email = user_data.get('email')
        user_update.name = user_data.get('name')
        user_update.surname = user_data.get('surname')
        user_update.password = self.get_hash(password_2)
        user_update.favorite_genre = user_data.get('favorite_genre')
        return self.dao.update(user_update)

    def part_update(self, user_data):
        user_update = self.get_one(user_data.get('id'))
        if user_data.get('email') is not None:
            user_update.email = user_data.get('email')
        if user_data.get('name') is not None:
            user_update.name = user_data.get('name')
        if user_data.get('surname') is not None:
            user_update.surname = user_data.get('surname')
        if user_data.get('favorite_genre') is not None:
            user_update.favorite_genre = user_data.get('favorite_genre')
        return self.dao.update(user_update)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def comprare_passwords(self, hash, password):
        decode_digest = base64.b64decode(hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decode_digest, hash_digest)



