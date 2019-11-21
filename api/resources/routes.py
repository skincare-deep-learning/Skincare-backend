from flask_restful import Resource
from flask import jsonify, request, json
import joblib
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import os

class Classifier(Resource):
    def get(self):
        return jsonify({'Method' : 'GET'})
    def post(self):
        try:
            file = request.files.get('file')
        except:
            return jsonify({'error': 'no file'}), 400
        
        return jsonify({"Name":file.filename})