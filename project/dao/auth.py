
from project.dao.models.user import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_find_username(self, email):
        """Ищем пользователя"""
        user = self.session.query(User).filter(User.email == email).first()
        data = {
            "username": user.username,
            "email": user.email,
            "password": user.password
        }
        return data
