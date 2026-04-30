from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.headline_ticker, name='headline_ticker'),    
]