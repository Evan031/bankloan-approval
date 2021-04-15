from django.urls import path
import app.views as views

app_name = 'app'

urlpatterns = [
    path('', views.model_form, name='model_form'),
]
