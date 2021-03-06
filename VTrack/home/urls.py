from django.urls import path
from . import views
from Users.views import register

urlpatterns = [
    path('', views.home, name='home'),
    path('howitworks/', views.howitworks, name='howitworks'),
    path('map/', views.map, name='map'),
    path('missingreport/', views.missingreport, name='missingreport'),
    path('register/', register, name='register'),
    path('route', views.routeModal, name='route'),
]
