from flask import Flask, app
from flask_cors import CORS
from flask_restx import Api

from project.config import Config
from project.setup_db import db
from project.views import genres_ns
from project.views.directors import director_ns
from project.views.movies import movie_ns
from project.views.users.users import user_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)

# Нужно для работы с фронтендом
cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(genres_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)

    return app

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()