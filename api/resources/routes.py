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


def make_dic(d):
    diseases = ['queratose actínica', 'angiofibroma', 'angioma', 'proliferação melanocítica atípica', 'carcinoma basocelular', 'dermatofibroma', 'lentigo NOS', 'lentigo simplex', 'queratose liquenóide', 'melanoma', 'Indefinido', 'Mancha', 'Outro Indefinido', 'queratose benigna pigmentada', 'Cicatriz', 'queratose seborreica', 'lentigo solar', 'carcinoma de células escamosas', 'lesão vascular']
    dis_list = []
    for x in np.nditer(d.T):
        dis_list.append(x)
    
        
    data = {
        'Diseases': diseases,
        'Probabilities': dis_list
    }

    df = pd.DataFrame(data, columns=['Diseases', 'Probabilities'])

    x = df.to_dict(orient='records')
    diseases_dict = json.dumps(x)
    print(diseases_dict)

    return diseases_dict


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
        data = make_dic(result)
        
        return jsonify({"Name":response.filename})