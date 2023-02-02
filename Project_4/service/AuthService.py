from flask import abort
import jwt
import datetime
import calendar

from helpers.constant import SECRET, ALGO
from service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        """
        Метод генерирует токены по username и password
        """
        user = self.user_service.get_by_email(email)
        if user is None:
            abort(400)
        if not is_refresh:
            if not self.user_service.comprare_passwords(user.password, password):
                abort(400)
        data = {
            "email": email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def aprove_refresh_token(self, token):
        """
        Метод генерирует токены по refresh_token
        """
        data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
        email = data.get("email")
        return self.generate_tokens(email, None, is_refresh=True)

    def create(self, data_request):
        return self.user_service.create(data_request)

    def check_register(self, email, password):
        if None in [email, password]:
            abort(400)
        user = self.user_service.get_by_email(email)
        if user is None:
            abort(401)
        if not self.user_service.comprare_passwords(user.password, password):
            abort(400)

        return True







