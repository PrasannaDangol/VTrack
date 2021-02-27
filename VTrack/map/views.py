from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Vehicle

@login_required
def map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoicHJhc2FubmExNzUwOSIsImEiOiJjazdiamt4cm8xZmp2M2VwamM4YW13aHZqIn0.Fyij8bD6WpqSnHAFL69yKA'
    a = '1'
    vehicle_location = Vehicle.objects.all()
    user_location = Profile.objects.all()

    context = {
    			'vehicle_location': vehicle_location,
    			'user_location': user_location,
    			'mapbox_access_token': mapbox_access_token,
    			'a': a
    		}

    return render(request, 'map/map.html', context : context)