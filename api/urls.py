from django.urls import path
import api.views as views

app_name = 'api'

urlpatterns = [
    path('', views.Model_Predict.as_view(), name='predict'),
]
