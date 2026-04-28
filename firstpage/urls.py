from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('user/<str:username>/', views.user_profile, name='user_profile'), #dynamic URL pattern
]


