from django.urls import path
from . import views

urlpatterns = [
    path('', views.missingreport, name='missingreport'),
]