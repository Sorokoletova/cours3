from project.dao.user import UserDAO
from project.utils import get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_id(self, nid):
        return self.dao.get_id(nid)

    def create(self, data):
        data["password"] = get_hash(data["password"])
        self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, nid):
        self.dao.delete(nid)

    def update_password(self, data):
        hash_password = get_hash(data['password'])
        if users['password'] != hash_password:
            abort(401, "Нет такого пароля")
        data["password_1"] = get_hash(data["password"])
        self.dao.update(data)