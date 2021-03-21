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
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            married = form.cleaned_data['married']
            dependents = form.cleaned_data['dependents']
            education = form.cleaned_data['education']
            self_employed = form.cleaned_data['self_employed']
            applicant_income = form.cleaned_data['applicant_income']
            coapplicant_income = form.cleaned_data['coapplicant_income']
            loan_amount = form.cleaned_data['loan_amount']
            loan_amount_term = form.cleaned_data['loan_amount_term']
            credit_history = form.cleaned_data['credit_history']
            property_area = form.cleaned_data['property_area']
            my_dict = (request.POST).dict()
            # print(my_dict)
            my_dict.pop('csrfmiddlewaretoken')
            answer = approvereject(my_dict)
            messages.success(request, f'Application Status: {answer}')

    form = ApprovalForm()

    return render(request, 'myform/model-form.html', {'form': form})
