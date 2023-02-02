from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, update_user):
        self.session.add(update_user)
        self.session.commit()
        return update_user

    def delete(self, uid):
        delete_user = self.get_one(uid)
        self.session.delete(delete_user)
        self.session.commit()

