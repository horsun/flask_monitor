from flask import jsonify
from flask_restful import Resource


class World(Resource):
    def get(self):
        return jsonify({"hell": 'world'})
