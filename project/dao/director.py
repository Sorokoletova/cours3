from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_all = self.session.query(Director)
        return director_all

    def get_id(self, nid):
        director = self.session.query(Director).filter(Director.id == nid).first()
        return director
