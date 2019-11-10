from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS, cross_origin
from api.resources.routes import Classifier

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(app)

api.add_resource(Classifier, '/classifier')
app.register_blueprint(api_bp)