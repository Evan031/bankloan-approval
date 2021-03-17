from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.ensemble import RandomForestClassifier

from .apps import ModelConfig
import pandas as pd


@api_view(['POST'])
def approvereject(request):
    try:
        data = request.data
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_classifier = ModelConfig.classifier
        y_pred = loaded_classifier.predict(X)
        y_pred = pd.Series(y_pred)
        target_map = {0: 'Rejected', 1: 'Approved'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {f'Your loan status is {y_pred[0]}'}
        return Response(response_dict, status=200)
    except ValueError as error:
        return (error.args[0])

# # @api_view(["POST"])
# def approvereject(unit):
# 	try:
# 		mdl=joblib.load("MyAPI/evan_loan_model.pkl")
# 		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
# 		# mydata=request.data
# 		# unit=np.array(list(mydata.values()))
# 		# unit=unit.reshape(1,-1)
# 		scalers=joblib.load("MyAPI/scalers.pkl")
# 		X=scalers.transform(unit)
# 		y_pred=mdl.predict(X)
# 		y_pred=(y_pred>0.58)
# 		newdf=pd.DataFrame(y_pred, columns=['Status'])
# 		newdf=newdf.replace({True:'Approved', False:'Rejected'})
# 		K.clear_session()
# 		return (newdf.values[0][0],X[0])
# 		print(newdf.values[0][0],X[0])
# 	except ValueError as e:
# 		return (e.args[0])
