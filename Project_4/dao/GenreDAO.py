from config import Config
from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page):
        if page is not None:
            page = int(page)
            return self.session.query(Genre).paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, update_genre):
        self.session.add(update_genre)
        self.session.commit()
        return update_genre

    def delete(self, gid):
        delete_genre = self.get_one(gid)
        self.session.delete(delete_genre)
        self.session.commit()