from django.shortcuts import render
from django.contrib import messages


def model_form(request):
    return render(request, 'myform/model-form.html')
