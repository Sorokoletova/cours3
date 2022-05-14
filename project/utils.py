import base64
import hashlib
import json
from datetime import datetime, timedelta

import jwt

from constants import PWD_HASH_NAME, PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET_KEY, AlGORITM


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


def generate_tokens(data):
    """Создаем пару токенов"""
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False
    access_token = jwt.encode(payload=data, key=SECRET_KEY, algorithm=AlGORITM)
    data['exp'] = datetime.utcnow() + timedelta(days=60)
    data['refresh_token'] = True
    refresh_token = jwt.encode(payload=data, key=SECRET_KEY, algorithm=AlGORITM)
    tokens_user = {"access_token": access_token, "refresh_token": refresh_token}

    return tokens_user, 201
