from django.urls import path
import app.views as views

urlpatterns = [
    path('model/', views.approvereject, name='model'),
    path('form/', views.cxcontact, name='cxform'),
]