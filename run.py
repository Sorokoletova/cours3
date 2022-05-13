from flask import Flask
from flask_restx import Api

from project.config import Config
from project.server import db
from project.views import genres_ns
from project.views.auth import auth_ns
from project.views.directors import director_ns
from project.views.movies import movie_ns
from project.views.users.users import user_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
