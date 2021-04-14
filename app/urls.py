from django.urls import path
import app.views as views

app_name = 'app'

urlpatterns = [
    path('', views.cxcontact, name='cxform'),
    path('predict/', views.Model_Predict.as_view(), name='predict'),
]
