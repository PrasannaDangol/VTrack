from mapbox import Directions
import json
from map.models import Vehicle

vehicle_number = Vehicle.objects.all()
print(vehicle_number)
service = Directions(
    access_token="pk.eyJ1IjoieHVqYW4xOTY2IiwiYSI6ImNrbHFtdXZycjB3cGsyb2xoY3hqaTRsenUifQ.XE2vYY9Ccowx9lipD08Wlw")

origin = {
    'type': 'Point',
    'coordinates': [85.297184, 27.698824]
}

destination = {
    'type': 'Point',
    'coordinates': [85.317117, 27.690491]
}

destination2 = {
    'type': 'Point',
    'coordinates': [85.3163048, 27.6810902]
}

response = service.directions([origin, destination, destination2], 'mapbox.driving')

driving_routes = response.geojson()
json_object = json.dumps(driving_routes['features'][0]['geometry']['coordinates'], indent=4)
directionCordinates = json_object