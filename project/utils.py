import base64
import hashlib
import json

from constants import PWD_HASH_NAME, PWD_HASH_SALT, PWD_HASH_ITERATIONS


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def get_hash(password):
    """Хешируем пароль"""
    new_password = hashlib.pbkdf2_hmac(
        hash_name=PWD_HASH_NAME,
        password=password.encode('utf-8'),
        salt=PWD_HASH_SALT,
        iterations=PWD_HASH_ITERATIONS)
    return base64.b64encode(new_password).decode('utf-8')
