from config import Config
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filter):
        status = filter.get('status')
        page = filter.get('page')
        if status == 'new' and page is not None:
            page = int(page)
            result = self.session.query(Movie).order_by(Movie.year.desc()).\
                paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
            return result
        elif status == 'new':
            return self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page is not None:
            page = int(page)
            return self.session.query(Movie).paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items

        return self.session.query(Movie).all()

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, update_movie):
        self.session.add(update_movie)
        self.session.commit()
        return update_movie

    def delete(self, mid):
        delete_movie = self.get_one(mid)
        self.session.delete(delete_movie)
        self.session.commit()
