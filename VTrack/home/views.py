from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from map.models import Vehicle
from .tests import *


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def howitworks(request):
    return render(request, 'home/howitworks.html')

@login_required
def map(request):
	mapbox_access_token = 'pk.eyJ1IjoicHJhc2FubmExNzUwOSIsImEiOiJjazdiamt4cm8xZmp2M2VwamM4YW13aHZqIn0.Fyij8bD6WpqSnHAFL69yKA'
	vehicle_number = Vehicle.objects.all()
	# vehicle_number = vehicle_number[0].licensenumber
	context = {
	"mapbox" : mapbox_access_token,
	"vehicle_number" : vehicle_number,
	"directionCordinate" : directionCordinates
	}
	return render(request, 'map/map.html', context)

@login_required
def missingreport(request):
    return render(request, 'missingreport/missingreport.html')