# from flask import request, abort
from flask import request, abort
from flask_restx import Resource, Namespace

from container import movie_service
from project.schemas.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieView(Resource):
#     @auth_required
     def get(self):
         args = request.args
         if 'status' in args:
             mov = movie_service.get_all_sort()
         elif 'page' in args:
             mov = movie_service.get_all().limit(12)
         elif 'page' in args and 'status' in args:
             mov = movie_service.get_all_sort().limit(12)
         else:
             mov = movie_service.get_all()
         return movies_schema.dump(mov), 200
#
#     @admin_required
#     def post(self):
#         movie = request.json
#         movie_service.create(movie)
#         return "", 201
#
#
@movie_ns.route("/<int:nid>")
class MovieView(Resource):
#     @auth_required
     def get(self, nid):
         movie = movie_service.get_id(nid)
         if movie is None:
             abort(404)
         return movie_schema.dump(movie), 200
#
#     @admin_required
#     def put(self, nid: int):
#         movie = request.json
#         movie['id'] = nid
#         movie_service.update(movie)
#         return "", 204
#
#     @admin_required
#     def delete(self, nid: int):
#         movie_service.delete(nid)
#         return "", 204
