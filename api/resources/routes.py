from flask_restful import Resource
from flask import jsonify

class Classifier(Resource):
    def get(self):
        return jsonify({'Method' : 'GET'})
    def post(self):
        return jsonify({'Method' : 'POST'})