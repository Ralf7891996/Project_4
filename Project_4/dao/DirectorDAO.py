from config import Config
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page):
        if page is not None:
            page = int(page)
            return self.session.query(Director).paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def create(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, update_director):
        self.session.add(update_director)
        self.session.commit()
        return update_director

    def delete(self, did):
        delete_director= self.get_one(did)
        self.session.delete(delete_director)
        self.session.commit()