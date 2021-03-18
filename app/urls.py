from django.urls import path
import app.views as views

urlpatterns = [
    path('', views.cxcontact, name='cxform'),
]
