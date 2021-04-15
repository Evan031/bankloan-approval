from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .apps import ModelConfig
import pandas as pd


class Model_Predict(APIView):
    def post(self, request, format=None):
        try:
            # If request is made directly to api this code will execute
            if type(request.data) is dict:
                data = request.data

            # If request is made through frontend code will execute
            else:
                data = request.data
                data = data.dict()
                data.pop('csrfmiddlewaretoken')
            keys = []
            values = []
            # Values are seperated from keys and placed in array
            for key in data:
                keys.append(key)
                values.append(int(data[key]))
            # Array is reshaped and then passed to model
            X = pd.Series(values).to_numpy().reshape(1, -1)
            loaded_classifier = ModelConfig.classifier
            y_pred = loaded_classifier.predict(X)
            # Model response is 0 or 1 that response is then made
            # human readable via target map
            y_pred = pd.Series(y_pred)
            target_map = {0: 'rejected', 1: 'approved'}
            # Target is mapped below
            y_pred = y_pred.map(target_map).to_numpy()
            # Response is created and returns dictionary
            response_dict = {"prediction": f"{y_pred[0]}"}
            return Response(response_dict, status=200)
        except ValueError as error:
            return (error.args[0], status.HTTP_400_BAD_REQUEST)
