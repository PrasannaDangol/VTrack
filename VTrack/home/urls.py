from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('howitworks/', views.howitworks, name='howitworks'),
    path('map/', views.map, name='map'),
]
