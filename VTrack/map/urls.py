from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.map_loc, name="map"),
]