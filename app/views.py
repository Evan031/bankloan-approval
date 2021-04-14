from django.shortcuts import render
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.ensemble import RandomForestClassifier
from . forms import ApprovalForm

from .apps import ModelConfig
import pandas as pd


class Model_Predict(APIView):
    def post(self, request, format=None):
        try:
            if type(request.data) is dict:
                data = request.data
            else:
                data = request.data
                data = data.dict()
                data.pop('csrfmiddlewaretoken')
            keys = []
            values = []
            for key in data:
                keys.append(key)
                values.append(int(data[key]))
            X = pd.Series(values).to_numpy().reshape(1, -1)
            loaded_classifier = ModelConfig.classifier
            y_pred = loaded_classifier.predict(X)
            y_pred = pd.Series(y_pred)
            target_map = {0: 'rejected', 1: 'approved'}
            y_pred = y_pred.map(target_map).to_numpy()
            response_dict = {"prediction": f"{y_pred[0]}"}
            return Response(response_dict, status=200)
        except ValueError as error:
            return (error.args[0], status.HTTP_400_BAD_REQUEST)


class Pkl_Model_Predict(APIView):
    def post(self, request, format=None):
        if type(request.data) is dict:
            data = request.data
        else:
            data = request.data
            data = data.dict()
            data.pop('csrfmiddlewaretoken')
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_classifier = NewConfig.classifier
        y_pred = loaded_classifier.predict(X)
        y_pred = pd.Series(y_pred)
        target_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"prediction": y_pred[0]}
        return Response(response_dict, status=200)

# @api_view(['POST'])


def approvereject(unit):
    try:
        data = unit
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(int(data[key]))
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_classifier = ModelConfig.classifier
        y_pred = loaded_classifier.predict(X)
        y_pred = pd.Series(y_pred)
        target_map = {0: 'Rejected', 1: 'Approved'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = y_pred[0]
        # response_dict = {f'Your loan status is {y_pred[0]}'}
        # return Response(response_dict, status=200)
        return response_dict
    except ValueError as error:
        return (error.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
    return render(request, 'myform/model-form.html')
