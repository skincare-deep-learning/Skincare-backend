from flask_restful import Resource
from flask import jsonify, request
import json
import numpy as np
import pandas as pd
from keras.preprocessing import image
from PIL import Image
import pickle
import joblib
from io import BytesIO
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import keras.backend.tensorflow_backend as tb


def set_diseases(d):
    diseases = ['Queratose actinica',  'Carcinoma basocelular',  'Melanoma', 'Indefinido', 'Mancha',  'Queratose benigna pigmentada',  'Queratose seborreica',  'Carcinoma de celulas escamosas', 'Lesao vascular']
    dis = d.reshape(19, 1)
    dis = dis.tolist()
    dict = {}
    for i in range(len(dis)):
        dict[diseases[i]] = dis[i][0]  
    json.dumps(dict)

    return dict

class Classifier(Resource):
    def post(self):
        tb._SYMBOLIC_SCOPE.value = True
        
        try:
            response = request.files.get('file')
        except:
            return jsonify({'error': 'no file'}), 400

        img = Image.open(response)
        img = img.resize((64, 64))
        test_image = image.img_to_array(img)/255
        test_image = np.expand_dims(test_image, axis=0)

        #Importing the classifier
        classifier = joblib.load('cnn_classifier.jb')

        #Making the prediction
        result = classifier.predict(test_image)

        data = set_diseases(result)
        
        return jsonify({"data":data})
