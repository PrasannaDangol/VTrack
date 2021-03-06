from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from map.models import Vehicle
from Users.models import Profile
from .models import MissingVehicle
from .emailsender import mailgun
from .tests import route
from .forms import *

# Create your views here
def routeModal(request):
	user_location = Profile.objects.all()
	print(user_location)
	if request.method == 'POST':
		if request.POST.get('mes'):
			savemessage = MissingVehicle()
			savemessage.licensenumber = user_location[0].licensenumber
			savemessage.mes = request.POST.get('mes')
			savemessage.email = request.POST.get('emailModal')
			savemessage.save()
			return render(request, 'home/home.html')
	else:
		return render(request, 'home/home.html')

def home(request):
    return render(request, 'home/home.html')

def howitworks(request):
    return render(request, 'home/howitworks.html')

@login_required
def map(request):
	mapbox_access_token = 'pk.eyJ1IjoicHJhc2FubmExNzUwOSIsImEiOiJjazdiamt4cm8xZmp2M2VwamM4YW13aHZqIn0.Fyij8bD6WpqSnHAFL69yKA'
	vehicle_number = Vehicle.objects.all()
	user_location = Profile.objects.all()

	# vehicle_number = vehicle_number[0].licensenumber
	context = {
	"mapbox" : mapbox_access_token,
	"vehicle_number" : vehicle_number,
	"directionCordinate" : route()
	}
	j=0
	for i in vehicle_number:
		if(vehicle_number[j].licensenumber == user_location[0].licensenumber):
			route()
			# mailgun.send_vehicle_found_message()
			print("sads")
		j += 1
	return render(request, 'map/map.html', context)

@login_required
def missingreport(request):
	message = "abc"
	mailgun.missing_report_message(message)
	return render(request, 'missingreport/missingreport.html')