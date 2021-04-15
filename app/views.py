from django.shortcuts import render
from django.contrib import messages


def model_form(request):
    return render(request, 'app/model_form.html')

# def template_example_1(request):
#     return render(request,"child_page_1.html")
