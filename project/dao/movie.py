from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies_all = self.session.query(Movie)
        return movies_all

    def get_id(self, nid):
        movie = self.session.query(Movie).filter(Movie.id == nid).first()
        return movie

    def get_all_sort(self):
        movies_all = self.session.query(Movie).order_by(Movie.year.desc()).all()
        return movies_all
