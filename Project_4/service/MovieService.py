
from dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, data_req):
        if data_req.get("genre_id") is not None:
            movies_query = self.dao.get_by_genre(data_req.get("genre_id"))
        elif data_req.get("director_id") is not None:
            movies_query = self.dao.get_by_director(data_req.get("director_id"))
        elif data_req.get("year") is not None:
            movies_query = self.dao.get_by_year(data_req.get("year"))
        else:
            movies_query = self.dao.get_all(data_req)
        return movies_query

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        update_movie = self.get_one(data.get("id"))
        update_movie.title = data.get("title")
        update_movie.description = data.get("description")
        update_movie.trailer = data.get("trailer")
        update_movie.year = data.get("year")
        update_movie.rating = data.get("rating")
        update_movie.genre_id = data.get("genre_id")
        update_movie.director_id = data.get("director_id")
        return self.dao.update(update_movie)

    def update_part(self, data):
        update_movie = self.get_one(data.get("id"))
        if data.get("title") is not None:
            update_movie.title = data.get("title")
        if data.get("description") is not None:
            update_movie.description = data.get("description")
        if data.get("trailer") is not None:
            update_movie.trailer = data.get("trailer")
        if data.get("year") is not None:
            update_movie.year = data.get("year")
        if data.get("rating") is not None:
            update_movie.rating = data.get("rating")
        if data.get("genre_id") is not None:
            update_movie.genre_id = data.get("genre_id")
        if data.get("director_id") is not None:
            update_movie.director_id = data.get("director_id")
        return self.dao.update(update_movie)

    def delete(self, mid):
        return self.dao.delete(mid)


