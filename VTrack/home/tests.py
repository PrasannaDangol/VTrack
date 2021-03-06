from mapbox import Directions
import json
from map.models import Vehicle
from Users.models import Profile

def route():
    user_location = Profile.objects.all()
    vehicle_number = Vehicle.objects.all()
    service = Directions(
        access_token="pk.eyJ1IjoieHVqYW4xOTY2IiwiYSI6ImNrbHFtdXZycjB3cGsyb2xoY3hqaTRsenUifQ.XE2vYY9Ccowx9lipD08Wlw")

    j=0
    a = 1
    desttemp = []
    for i in vehicle_number:
        if(vehicle_number[j].licensenumber == user_location[0].licensenumber):
            a = a + 1
            dest = "destination" + str(a)
            dest = {
                'type': 'Point',
                'coordinates': [float(i.lon), float(i.lat)]
            }
            desttemp.append(dest)
        j += 1
    if(desttemp != [] and len(desttemp)!= 1):
        response = service.directions(desttemp, 'mapbox.driving')
        driving_routes = response.geojson()
        json_object = json.dumps(driving_routes['features'][0]['geometry']['coordinates'], indent=4)
        directionCordinates = json_object
        return directionCordinates
    else:
        directionCordinates = {}
        return directionCordinates
